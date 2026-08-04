"""
RanZiz AI Runtime Trace
Version 1.0
"""


from datetime import UTC, datetime


class RuntimeTrace:

    def __init__(self):

        self.records = []


    def record(
        self,
        event,
        state=None,
        capability=None,
        payload=None
    ):

        self.records.append({

            "event": event,

            "state": state,

            "capability": capability,

            "payload": payload or {},

            "timestamp": datetime.now(
                UTC
            ).isoformat()

        })


    def all(self):

        return list(
            self.records
        )


    def last(self):

        if not self.records:
            return None

        return self.records[-1]


    def clear(self):

        self.records.clear()


    def __len__(self):

        return len(
            self.records
        )


    def __repr__(self):

        return (
            f"RuntimeTrace("
            f"{len(self)} records)"
        )
