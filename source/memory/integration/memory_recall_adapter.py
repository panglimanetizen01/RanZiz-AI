"""
RanZiz AI Memory Recall Adapter
Version 2.0
"""

from source.memory.memory_repository import MemoryRepository
from source.memory.provider.memory_context_provider import MemoryContextProvider


class MemoryRecallAdapter:

    def __init__(self):

        self.provider = MemoryContextProvider()

        self.repository = MemoryRepository()

    def recall(

        self,

        key

    ):

        result = self.repository.get(

            key

        )

        if result is None:

            return None

        return f"{key} = {result}"

    def identity(self):

        return self.provider.get_identity_context()

    def profile(self):

        return self.provider.get_context(

            "nama"

        )

    def __repr__(self):

        return "MemoryRecallAdapter()"