"""
RanZiz AI Memory Recall Engine
Version 2.0
"""

from source.memory.search.memory_search import MemorySearch


class MemoryRecallEngine:

    MAX_RESULTS = 20

    def __init__(self):

        self.search = MemorySearch()

    def process(

        self,

        message

    ):

        if not isinstance(message, str):

            return None

        text = message.lower().strip()

        if not text:

            return None

        if "apa yang kamu ingat" in text:

            memories = self.search.all()

            if not isinstance(memories, dict):

                return None

            if not memories:

                return None

            lines = [
                "Saya mengingat:"
            ]

            for count, (key, value) in enumerate(
                memories.items(),
                start=1,
            ):

                lines.append(
                    f"- {key}: {value}"
                )

                if count >= self.MAX_RESULTS:

                    remaining = len(memories) - count

                    if remaining > 0:

                        lines.append(
                            f"... dan {remaining} data lainnya."
                        )

                    break

            return "\n".join(lines)

        patterns = {

            "nama": "nama",
            "genre": "genre",
            "warna": "warna",
            "hobi": "hobi",
            "kota": "kota"

        }

        for keyword, memory_key in patterns.items():

            if keyword not in text:

                continue

            result = self.search.find(
                memory_key
            )

            if not isinstance(result, dict):

                continue

            if not result:

                continue

            key = next(iter(result))

            return f"{key} = {result[key]}"

        return None

    def __repr__(self):

        return "MemoryRecallEngine()"
