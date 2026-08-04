"""
RanZiz AI Capability Runtime
Version 4.0
"""

from source.capability.scheduler.capability_scheduler import (
    CapabilityScheduler,
)
from source.runtime.context.execution_context import ExecutionContext
from source.runtime.events.runtime_event_bus import RuntimeEventBus
from source.runtime.retry.retry_executor import RetryExecutor
from source.runtime.retry.retry_policy import RetryPolicy
from source.runtime.state.runtime_state import RuntimeState


class CapabilityRuntime:

    def __init__(self):

        self.scheduler = CapabilityScheduler()
        self.events = RuntimeEventBus()
        self.state = RuntimeState()

    def execute(
        self,
        plan,
        payload
    ):

        self.events.clear()
        self.state.transition("PLANNING")
        self.events.emit("PLAN_STARTED")

        self.state.transition("RUNNING")

        results = {}

        context = ExecutionContext(
            payload.get(
                "context",
                {}
            )
        )

        while not self.scheduler.finished(plan):

            ready = self.scheduler.ready(plan)

            if not ready:
                break

            for item in ready:

                name = item["name"]
                executor = RetryExecutor(
                    item["executor"],
                    RetryPolicy(3)
                )

                plan.set_status(
                    name,
                    "RUNNING"
                )

                self.events.emit(
                    "CAPABILITY_STARTED",
                    name
                )

                try:

                    execution_payload = dict(payload)
                    execution_payload["context"] = context

                    result = executor.execute(
                        execution_payload
                    )

                    context.set(
                        name,
                        result
                    )

                    plan.set_result(
                        name,
                        result
                    )

                    plan.set_status(
                        name,
                        "SUCCESS"
                    )

                    self.events.emit(
                        "CAPABILITY_COMPLETED",
                        name,
                        {
                            "status": "SUCCESS"
                        }
                    )

                    results[name] = result

                except Exception as error:  # noqa: BLE001

                    message = {
                        "error": str(error)
                    }

                    plan.set_result(
                        name,
                        message
                    )

                    plan.set_status(
                        name,
                        "FAILED"
                    )

                    self.events.emit(
                        "CAPABILITY_FAILED",
                        name,
                        message
                    )

                    results[name] = message

            if self.scheduler.failed(plan):
                break

        self.state.transition("COMPLETED")
        self.events.emit("PLAN_COMPLETED")

        return results
