"""
RanZiz AI Memory Updater
Version 1.1
"""

from source.memory.memory_repository import MemoryRepository


class MemoryUpdater:

    def __init__(self):

        self.repository = MemoryRepository()

    def update(

        self,

        key,

        value

    ):

        return self.repository.save(

            key,

            value

        )

    def get(

        self,

        key,

        default=None

    ):

        return self.repository.get(

            key,

            default

        )

    def exists(

        self,

        key

    ):

        return self.repository.exists(

            key

        )

    def all(self):

        return self.repository.all()

    def __repr__(self):

        return "MemoryUpdater()"