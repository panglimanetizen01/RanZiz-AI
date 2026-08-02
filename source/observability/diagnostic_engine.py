"""
RanZiz AI Diagnostic Engine
Version 1.0
"""

from source.logging.error_analyzer import ErrorAnalyzer


class DiagnosticEngine:


    def __init__(self):

        self.error_analyzer = ErrorAnalyzer()



    def analyze(

        self,

        trace

    ):

        diagnosis = self.error_analyzer.analyze(
            trace
        )


        result = {

            "status": "SUCCESS",

            "failure_point": None,

            "possible_cause": None,

            "recommendation": None

        }


        if diagnosis["has_error"]:

            result["status"] = "FAILED"


            result["failure_point"] = (
                diagnosis["failure_point"]
            )


            result["possible_cause"] = (
                diagnosis["possible_cause"]
            )


            result["recommendation"] = (
                self.recommend(
                    diagnosis
                )
            )


        return result



    def recommend(

        self,

        diagnosis

    ):

        point = diagnosis.get(
            "failure_point"
        )


        if point:

            return (
                f"Periksa modul {point} "
                "dan validasi input/output."
            )


        return (
            "Periksa trace sistem "
            "untuk menemukan sumber masalah."
        )