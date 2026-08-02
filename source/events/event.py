"""
RanZiz AI Event
Version 1.0
"""

from datetime import UTC, datetime


class Event:


    def __init__(

        self,

        name,

        payload=None

    ):

        self.name = name

        self.payload = payload or {}

        self.timestamp = (
            datetime.now(UTC).isoformat()
        )


    def to_dict(self):

        return {

            "name": self.name,

            "payload": self.payload,

            "timestamp": self.timestamp

        }


    def __repr__(self):

        return (
            f"Event({self.name})"
        )