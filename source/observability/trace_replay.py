"""
RanZiz AI Trace Replay
Version 1.2
"""

import json


class TraceReplay:

    def load(self, filepath):
        with open(
            filepath,
            "r",
            encoding="utf-8"
        ) as f:
            return json.load(f)

    def replay(
        self,
        filepath,
        event_filter=None
    ):
        data = self.load(filepath)

        timeline = data.get(
            "timeline",
            ""
        )

        for line in timeline.splitlines():

            if event_filter:

                parts = line.split("|")

                if len(parts) < 2:
                    continue

                event = parts[1].strip()

                if not event.startswith(event_filter):
                    continue

            yield line
