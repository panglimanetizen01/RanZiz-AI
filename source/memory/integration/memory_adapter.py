"""
RanZiz AI Memory Adapter
Version 1.1
"""

from source.memory.provider.memory_context_provider import MemoryContextProvider


class MemoryAdapter:


    def __init__(self):

        self.provider = MemoryContextProvider()



    def get_context(

        self,

        key

    ):

        return self.provider.get_context(

            key

        )



    def get_identity_context(

        self

    ):

        return self.provider.get_identity_context()



    def enrich(

        self,

        message

    ):

        lower = message.lower()


        if "siapa nama saya" in lower:

            return self.get_context(

                "nama"

            )


        if "apa yang kamu ingat tentang saya" in lower:

            return self.get_identity_context()


        return None



    def __repr__(self):

        return "MemoryAdapter()"