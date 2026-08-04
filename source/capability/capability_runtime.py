"""
RanZiz AI Capability Runtime
Version 3.0
"""

from source.capability.scheduler.capability_scheduler import (
    CapabilityScheduler,
)
from source.runtime.context.execution_context import ExecutionContext


class CapabilityRuntime:

    def __init__(self):

        self.scheduler = CapabilityScheduler()

    def execute(
        self,
        plan,
        payload
    ):

        results = {}

        context = ExecutionContext(
            payload.get(
                "context",
                {}
            )
        )

        while not self.scheduler.finished(plan):

            ready = self.scheduler.ready(
                plan
            )

            if not ready:
                break

            for item in ready:

                name = item["name"]
                executor = item["executor"]

                plan.set_status(
                    name,
                    "RUNNING"
                )

                try:

                    execution_payload = dict(
                        payload
                    )

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

                    results[name] = message

            if self.scheduler.failed(
                plan
            ):
                break

        return results
