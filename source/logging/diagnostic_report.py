"""
RanZiz AI Diagnostic Report
Version 1.1
"""


class DiagnosticReport:



    def build(

        self,

        summary,

        diagnosis=None

    ):

        lines = []


        lines.append("=" * 50)
        lines.append("RanZiz AI Diagnostic Report")
        lines.append("=" * 50)


        lines.append("")


        lines.append(
            f"Request ID : {summary['request_id']}"
        )


        lines.append(
            f"Status     : {summary['status']}"
        )


        lines.append(
            f"Agent      : {summary['agent']}"
        )


        lines.append(
            f"Workflow   : {summary['workflow']}"
        )


        lines.append("")

        lines.append("Capabilities")


        for capability in summary["capabilities"]:

            lines.append(
                f"  ✓ {capability}"
            )


        metrics = summary.get(
            "metrics",
            {}
        )

        durations = metrics.get(
            "capability_duration",
            {}
        )

        if durations:

            lines.append("")

            lines.append(
                "Performance"
            )

            for capability, duration in durations.items():

                lines.append(
                    f"  {capability} : {duration} ms"
                )


        if diagnosis is not None:


            lines.append("")


            lines.append(
                "Diagnosis"
            )


            lines.append(
                f"  Status          : {diagnosis.get('status')}"
            )


            if diagnosis.get("failure_point"):

                lines.append(
                    f"  Failure Point   : {diagnosis.get('failure_point')}"
                )


            if diagnosis.get("possible_cause"):

                lines.append(
                    f"  Possible Cause  : {diagnosis.get('possible_cause')}"
                )


            if diagnosis.get("recommendation"):

                lines.append(
                    f"  Recommendation  : {diagnosis.get('recommendation')}"
                )


        lines.append("")


        lines.append(
            f"Total Events : {summary['total_events']}"
        )


        lines.append(
            f"Total Errors : {summary['total_errors']}"
        )


        lines.append("")


        lines.append("=" * 50)


        return "\n".join(lines)