"""
RanZiz AI Trace Analyzer
Version 1.1
"""


class TraceAnalyzer:

    def analyze(self, trace):

        report = {
            "status": "SUCCESS",
            "agent": None,
            "workflow": None,
            "capabilities": [],
            "errors": []
        }

        for item in trace:

            event = item.get("event")
            data = item.get("data", {})

            if event == "agent.selected":

                report["agent"] = data.get("agent")

            elif event in (

                "workflow.selected",
                "workflow.started"

            ):

                report["workflow"] = data.get("workflow")

            elif event in (

                "capability.started",
                "capability.finished"

            ):

                capability = data.get("capability")

                if capability and capability not in report["capabilities"]:

                    report["capabilities"].append(capability)

            elif event == "error.occurred":

                report["status"] = "FAILED"

                report["errors"].append(data)

        return report