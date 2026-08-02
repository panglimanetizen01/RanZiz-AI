"""
RanZiz AI Memory Decay System
Version 1.0
"""

from datetime import UTC, datetime


class MemoryDecay:


    def calculate(

        self,

        memory,

        current_time=None

    ):

        if current_time is None:

            current_time = datetime.now(UTC)



        created_at = memory.get(
            "created_at"
        )


        priority = memory.get(
            "priority",
            5
        )


        if created_at is None:

            return priority



        created_time = datetime.fromisoformat(
            created_at
        )


        age_days = (
            current_time - created_time
        ).days



        decay = age_days * 0.1


        score = priority - decay



        score = max(score, 0)



        return round(

            score,

            2

        )



    def apply(

        self,

        memories

    ):

        result = {}


        for key, memory in memories.items():

            if isinstance(memory, dict):

                result[key] = self.calculate(
                    memory
                )


        return result



    def __repr__(self):

        return "MemoryDecay()"