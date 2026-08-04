"""
RanZiz AI Runtime Event
Version 1.0
"""


class RuntimeEvent:

    def __init__(
        self,
        event,
        capability=None,
        payload=None
    ):

        self.event = event

        self.capability = capability

        self.payload = payload or {}

    def to_dict(self):

        return {

            "event": self.event,

            "capability": self.capability,

            "payload": self.payload

        }

    def __repr__(self):

        if self.capability:

            return (
                f"{self.event}"
                f"({self.capability})"
            )

        return self.event
