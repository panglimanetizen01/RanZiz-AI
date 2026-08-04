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
from source.runtime.trace.runtime_trace import RuntimeTrace
from source.runtime.snapshot.runtime_snapshot import RuntimeSnapshot


class CapabilityRuntime:

    def __init__(self):

        self.scheduler = CapabilityScheduler()
        self.events = RuntimeEventBus()
        self.state = RuntimeState()
        self.trace = RuntimeTrace()
        self.snapshot = RuntimeSnapshot()

    def execute(
        self,
        plan,
        payload
    ):

        self.events.clear()
        self.trace.clear()
        self.state.transition("PLANNING")
        self.trace.record(
            "PLAN_STARTED",
            self.state.current
        )
        self.events.emit("PLAN_STARTED")

        self.state.transition("RUNNING")

        results = {}

        context = ExecutionContext(
            payload.get(
                "context",
                {}
            )
        )

        self.snapshot.capture(
            self.state.current,
            plan,
            context
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

                self.trace.record(
                    "CAPABILITY_STARTED",
                    self.state.current,
                    name
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

                    self.trace.record(
                        "CAPABILITY_COMPLETED",
                        self.state.current,
                        name,
                        {
                            "status": "SUCCESS"
                        }
                    )

                    self.events.emit(
                        "CAPABILITY_COMPLETED",
                        name,
                        {
                            "status": "SUCCESS"
                        }
                    )

                    results[name] = result

                    self.snapshot.capture(
                        self.state.current,
                        plan,
                        context
                    )

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

                    self.trace.record(
                        "CAPABILITY_FAILED",
                        self.state.current,
                        name,
                        message
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
        self.trace.record(
            "PLAN_COMPLETED",
            self.state.current
        )

        self.snapshot.capture(
            self.state.current,
            plan,
            context
        )

        self.events.emit("PLAN_COMPLETED")

        return results
