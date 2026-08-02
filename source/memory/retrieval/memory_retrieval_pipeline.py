"""
RanZiz AI Memory Retrieval Pipeline
Version 2.1
"""


from source.memory.manager.memory_manager import MemoryManager
from source.memory.provider.memory_context_provider import MemoryContextProvider
from source.memory.search.memory_search import MemorySearch
from source.memory.semantic.memory_semantic import MemorySemantic


class MemoryRetrievalPipeline:


    def __init__(self):

        self.manager = MemoryManager()

        self.search = MemorySearch()

        self.context = MemoryContextProvider()

        self.semantic = MemorySemantic()



    def retrieve(
        self,
        message
    ):


        text = message.lower()



        # ==========================================
        # Semantic Memory
        # ==========================================

        semantic = self.semantic.match(
            text
        )


        if semantic:


            first = next(
                iter(
                    semantic.values()
                )
            )


            if isinstance(
                first,
                dict
            ):

                return first.get(
                    "value"
                )


            return str(
                first
            )



        # ==========================================
        # Rule Based (Fallback)
        # ==========================================


        if "nama" in text:

            return self.manager.get(
                "nama"
            )



        if (

            "kota" in text

            or "tinggal" in text

            or "di mana" in text

            or "dimana" in text

            or "alamat" in text

        ):

            return self.manager.get(
                "kota"
            )



        if "umur" in text:

            return self.manager.get(
                "umur"
            )



        if "hobi" in text:

            return self.manager.get(
                "hobi"
            )



        if (

            "genre" in text

            or "dangdut" in text

            or "favorit" in text

        ):

            return self.manager.get(
                "favorite_genre"
            )



        if (

            "profil" in text

            or "ingat" in text

            or "tentang saya" in text

        ):

            return self.context.get_identity_context()



        return None



    def __repr__(self):

        return "MemoryRetrievalPipeline()"