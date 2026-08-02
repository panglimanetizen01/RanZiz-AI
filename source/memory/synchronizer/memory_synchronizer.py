"""
RanZiz AI Memory Synchronizer
Version 2.0
"""

from source.memory.history.memory_history import MemoryHistory
from source.memory.memory_repository import MemoryRepository
from source.memory.update.memory_updater import MemoryUpdater


class MemorySynchronizer:

    def __init__(self):

        self.updater = MemoryUpdater()

        self.repository = MemoryRepository()

        self.history = MemoryHistory()

        self.rules = {

            "nama": [

                "username"

            ],

            "username": [

                "nama"

            ]

        }

    def _save(

        self,

        key,

        value

    ):

        old_value = self.repository.get(

            key

        )

        result = self.updater.update(

            key,

            value

        )

        if old_value != value:

            self.history.record(

                key,

                old_value,

                value

            )

        return result

    def sync(

        self,

        key,

        value

    ):

        updated = {}

        updated[key] = self._save(

            key,

            value

        )

        aliases = self.rules.get(

            key,

            []

        )

        for alias in aliases:

            updated[alias] = self._save(

                alias,

                value

            )

        return updated

    def __repr__(self):

        return "MemorySynchronizer()"