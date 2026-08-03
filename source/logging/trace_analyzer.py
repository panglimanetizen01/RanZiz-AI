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
            "errors": [],
            "metrics": {
                "total_events": len(trace),
                "retry_count": 0,
                "capability_duration": {}
            }
        }

        started = {}

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

            elif event == "retry.attempt":

                report["metrics"]["retry_count"] += 1


            elif event == "capability.started":

                capability = data.get("capability")

                if capability and capability not in report["capabilities"]:

                    report["capabilities"].append(capability)

                if capability:

                    started[capability] = item.get(
                        "elapsed_ms",
                        0
                    )


            elif event == "capability.finished":

                capability = data.get("capability")

                if capability and capability in started:

                    duration = (
                        item.get(
                            "elapsed_ms",
                            0
                        )
                        -
                        started[capability]
                    )

                    report["metrics"]["capability_duration"][capability] = round(
                        duration,
                        3
                    )

            elif event == "error.occurred":

                report["status"] = "FAILED"

                report["errors"].append(data)

        return report