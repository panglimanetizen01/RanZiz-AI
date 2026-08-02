"""
RanZiz AI Memory Reasoning
Version 1.0
"""

from source.memory.memory_service import MemoryService


class MemoryReasoning:


    def __init__(self):

        self.memory = MemoryService()


    def profile(self):

        memories = self.memory.memories()

        lines = []

        order = [

            "nama",

            "username",

            "umur",

            "kota",

            "hobi",

            "favorite_genre"

        ]

        labels = {

            "nama": "Nama",

            "username": "Username",

            "umur": "Umur",

            "kota": "Kota",

            "hobi": "Hobi",

            "favorite_genre": "Genre favorit"

        }

        for key in order:

            if key not in memories:

                continue

            value = memories[key]

            if isinstance(value, dict):

                value = value.get(

                    "value",

                    ""

                )

            if value in (

                None,

                ""

            ):

                continue

            lines.append(

                f"{labels[key]}: {value}"

            )

        return "\n".join(

            lines

        )


    def about_user(self):

        text = self.profile()

        if text:

            return text

        return "Saya belum memiliki informasi tentang Anda."


    def __repr__(self):

        return "MemoryReasoning()"