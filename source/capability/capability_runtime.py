"""
RanZiz AI Capability Runtime
Version 2.0
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

            try:

                execution_payload = dict(payload)

                execution_payload["context"] = context

                result = executor.execute(
                    execution_payload
                )

                results[name] = result

                context.set(
                    name,
                    result
                )

            except Exception as error:  # noqa: BLE001

                results[name] = {
                    "error": str(error)
                }

        return results
