"""
RanZiz AI Memory Service
Version 2.0
"""

from src.memory.memory_repository import MemoryRepository


class MemoryService:

    def __init__(self):

        self.repository = MemoryRepository()

    def remember(

        self,

        key,

        value

    ):

        if key is None:

            return None

        key = str(key).strip()

        if not key:

            return None

        if value is None:

            return None

        old_value = self.repository.get(key)

        if old_value == value:

            return self.repository.all().get(key)

        return self.repository.save(

            key,

            value

        )

    def recall(

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

    def forget(

        self,

        key

    ):

        return self.repository.delete(

            key

        )

    def memories(self):

        return self.repository.list()

    def all(self):

        return self.repository.all()

    def count(self):

        return len(

            self.repository.all()

        )

    def clear(self):

        memories = list(

            self.repository.all().keys()

        )

        for key in memories:

            self.repository.delete(

                key

            )

        return True

    def __repr__(self):

        return "MemoryService()"