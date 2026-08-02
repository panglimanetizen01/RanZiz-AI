"""
RanZiz AI Error Analyzer
Version 1.0
"""


class ErrorAnalyzer:


    def analyze(

        self,

        trace

    ):

        result = {

            "has_error": False,

            "errors": [],

            "failure_point": None,

            "possible_cause": None

        }


        if not trace:

            return result



        for event in trace:


            name = event.get(
                "event",
                ""
            )


            if (
                "error" in name.lower()
                or
                "failed" in name.lower()
            ):


                result["has_error"] = True


                data = event.get(
                    "data",
                    {}
                )


                result["errors"].append(
                    data
                )


                if "capability" in data:

                    result["failure_point"] = (
                        data["capability"]
                    )


                elif "module" in data:

                    result["failure_point"] = (
                        data["module"]
                    )


                if "error" in data:

                    result["possible_cause"] = (
                        data["error"]
                    )


        return result