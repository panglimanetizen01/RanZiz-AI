"""
RanZiz AI Memory Importance Engine
Version 1.0
"""


class MemoryImportance:


    def calculate(

        self,

        memory

    ):

        if not isinstance(memory, dict):

            return 0


        priority = memory.get(

            "priority",

            0

        )


        frequency = memory.get(

            "frequency",

            0

        )


        category = memory.get(

            "category",

            ""

        )


        score = priority + frequency


        if category == "identity":

            score += 20


        elif category == "project":

            score += 15


        elif category == "preference":

            score += 10


        return score



    def rank(

        self,

        memories

    ):

        result = {}


        for key, item in memories.items():

            result[key] = self.calculate(

                item

            )


        return dict(

            sorted(

                result.items(),

                key=lambda x: x[1],

                reverse=True

            )

        )



    def __repr__(self):

        return "MemoryImportance()"