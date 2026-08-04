"""
RanZiz AI Capability Runtime
Version 2.1
"""

from source.runtime.context.execution_context import ExecutionContext


class CapabilityRuntime:

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

        for item in plan:

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

        return results
