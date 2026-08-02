"""
RanZiz AI Capability Runtime
Version 1.1
"""


class CapabilityRuntime:


    def execute(
        self,
        plan,
        payload
    ):

        results = {}

        context = dict(
            payload.get(
                "context",
                {}
            )
        )


        for item in plan:

            name = item["name"]

            executor = item["executor"]


            try:

                execution_payload = dict(
                    payload
                )

                execution_payload["context"] = context


                result = executor.execute(
                    execution_payload
                )


                results[name] = result


                context[name] = result


            except Exception as error:  # noqa: BLE001
                # Isolate capability failures so remaining capabilities can continue.
                results[name] = {
                    "error": str(error)
                }


        return results