"""
RanZiz AI Response Builder
Version 1.2
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

        if hasattr(response, "output"):
            result = response.output

        elif isinstance(
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

                        outputs.append(
                            item.get(
                                "output",
                                ""
                            )
                        )

                result = "\n\n".join(
                    outputs
                )


        return result