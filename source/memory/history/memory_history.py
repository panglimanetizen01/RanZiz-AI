"""
RanZiz AI Memory History
Version 1.0
"""

from datetime import UTC, datetime

from source.database.database_manager import DatabaseManager


class MemoryHistory:

    def __init__(self):

        self.database = DatabaseManager()

    def record(

        self,

        key,

        old_value,

        new_value

    ):

        data = self.database.load()

        history = data.setdefault(

            "memory_history",

            {}

        )

        entries = history.setdefault(

            key,

            []

        )

        entries.append(

            {

                "timestamp": datetime.now(UTC).isoformat(),

                "old": old_value,

                "new": new_value

            }

        )

        self.database.save(

            data

        )

        return entries[-1]

    def get(

        self,

        key

    ):

        data = self.database.load()

        return data.get(

            "memory_history",

            {}

        ).get(

            key,

            []

        )

    def all(self):

        data = self.database.load()

        return data.get(

            "memory_history",

            {}

        )

    def clear(

        self,

        key=None

    ):

        data = self.database.load()

        history = data.setdefault(

            "memory_history",

            {}

        )

        if key is None:

            history.clear()

        else:

            history.pop(

                key,

                None

            )

        self.database.save(

            data

        )

        return True

    def __repr__(self):

        return "MemoryHistory()"