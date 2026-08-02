"""
RanZiz AI Memory Manager
Version 3.0
"""

from source.memory.consolidation.memory_consolidator import MemoryConsolidator
from source.memory.router.memory_router import MemoryRouter
from source.memory.synchronizer.memory_synchronizer import MemorySynchronizer


class MemoryManager:


    def __init__(self):

        self.synchronizer = MemorySynchronizer()

        self.router = MemoryRouter()

        self.consolidator = MemoryConsolidator()



    def save(

        self,

        key,

        value

    ):

        result = self.synchronizer.sync(

            key,

            value

        )


        if isinstance(result, dict):

            result = self.consolidator.consolidate(

                result

            )


        return result



    def get(

        self,

        key,

        default=None

    ):

        return self.synchronizer.updater.get(

            key,

            default

        )



    def exists(

        self,

        key

    ):

        return self.synchronizer.updater.exists(

            key

        )



    def all(self):

        return self.synchronizer.updater.all()



    def ask(

        self,

        message

    ):

        return self.router.route(

            message

        )



    def consolidate(self):

        memories = self.all()

        return self.consolidator.consolidate(

            memories

        )



    def __repr__(self):

        return "MemoryManager()"