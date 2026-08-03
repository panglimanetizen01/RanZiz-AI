"""
RanZiz AI Response Builder
Version 1.3
"""


class ResponseBuilder:


    def build(
        self,
        session_id,
        context,
        response,
        observability=None
    ):

        result = response


        if isinstance(
            response,
            dict
        ):

            if "output" in response:

                result = response["output"]


            elif "results" in response:

                outputs = []

                for item in response["results"]:

                    if isinstance(
                        item,
                        dict
                    ):

                        output = item.get(
                            "output",
                            ""
                        )

                        if isinstance(
                            output,
                            dict
                        ):
                            output = str(
                                output
                            )

                        outputs.append(
                            output
                        )

                result = "\n\n".join(
                    outputs
                )


            elif "result" in response and isinstance(
                response["result"],
                dict
            ):

                outputs = []

                for name, value in response["result"].items():

                    outputs.append(
                        f"{name}\n\n{value}"
                    )

                result = "\n\n".join(
                    outputs
                )


        return result
