"""
RanZiz AI Trace Viewer
Version 1.0
"""


class TraceViewer:

    def render(self, trace):

        lines = []

        for item in trace:

            elapsed = item.get(
                "elapsed_ms",
                0
            )

            event = item.get(
                "event",
                "-"
            )

            data = item.get(
                "data",
                {}
            )

            info = []

            for key, value in data.items():

                info.append(
                    f"{key}={value}"
                )

            detail = ""

            if info:

                detail = " | " + ", ".join(info)

            lines.append(
                f"{elapsed:8.3f} ms | {event}{detail}"
            )

        return "\n".join(lines)
