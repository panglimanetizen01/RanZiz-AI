"""
RanZiz AI Health Monitor
Version 1.0
"""


class HealthMonitor:


    def check(self, trace):

        warnings = []

        events = [
            item["event"]
            for item in trace
        ]


        if "request.created" not in events:

            warnings.append(
                "Request tidak pernah dibuat."
            )


        if (
            "workflow.started" in events
            and
            "workflow.finished" not in events
        ):

            warnings.append(
                "Workflow dimulai tetapi tidak selesai."
            )


        started = [

            item["data"].get("capability")

            for item in trace

            if item["event"] == "capability.started"

        ]


        finished = [

            item["data"].get("capability")

            for item in trace

            if item["event"] == "capability.finished"

        ]


        for capability in started:

            if capability not in finished:

                warnings.append(

                    f"Capability '{capability}' belum selesai."

                )


        return {

            "healthy": len(warnings) == 0,

            "warnings": warnings

        }