"""
RanZiz AI Log Entry
Version 1.0
"""


from datetime import UTC, datetime


class LogEntry:

    def __init__(
        self,
        level,
        category,
        message,
        metadata=None
    ):

        self.timestamp = datetime.now(UTC).isoformat()

        self.level = level

        self.category = category

        self.message = message

        self.metadata = metadata or {}


    def to_dict(self):

        return {

            "timestamp": self.timestamp,

            "level": self.level,

            "category": self.category,

            "message": self.message,

            "metadata": self.metadata

        }


    def __repr__(self):

        return (

            f"LogEntry("

            f"{self.level}, "

            f"{self.category})"

        )