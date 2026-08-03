"""
RanZiz AI Request Summary
Version 1.0
"""


class RequestSummary:


    def build(self, analysis, trace):

        return {

            "request_id": (

                trace[0]["request_id"]

                if trace else None

            ),

            "status": analysis["status"],

            "agent": analysis["agent"],

            "workflow": analysis["workflow"],

            "capabilities": list(
                analysis["capabilities"]
            ),

            "total_events": len(
                trace
            ),

            "total_errors": len(
                analysis["errors"]
            ),

            "metrics": analysis.get(
                "metrics",
                {}
            )

        }