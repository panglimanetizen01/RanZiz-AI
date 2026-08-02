"""
RanZiz AI Memory Semantic
Version 1.0
"""

from source.memory.search.memory_search import MemorySearch


class MemorySemantic:

    def __init__(self):

        self.search = MemorySearch()

        self.synonyms = {

            "nama": [
                "nama",
                "namaku",
                "dipanggil",
                "panggilan",
                "identitas"
            ],

            "kota": [
                "kota",
                "tinggal",
                "domisili",
                "alamat",
                "berasal",
                "di mana",
                "dimana"
            ],

            "umur": [
                "umur",
                "usia",
                "age"
            ],

            "hobi": [
                "hobi",
                "kesukaan",
                "suka"
            ],

            "favorite_genre": [
                "genre",
                "musik",
                "dangdut",
                "favorit"
            ]
        }

    def match(

        self,

        message

    ):

        text = message.lower()

        for key, words in self.synonyms.items():

            for word in words:

                if word in text:

                    result = self.search.find(

                        key

                    )

                    if result:

                        return result

        return {}

    def __repr__(self):

        return "MemorySemantic()"