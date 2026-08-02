"""
RanZiz AI Memory Priority
Version 1.0
"""


class MemoryPriority:


    def calculate(

        self,

        key,

        category=None

    ):

        name = key.lower()


        if category == "identity":

            return 10


        if category == "project":

            return 9


        if category == "preference":

            return 8



        if any(

            word in name

            for word in [

                "nama",

                "username",

                "umur",

                "kota"

            ]

        ):

            return 10



        if any(

            word in name

            for word in [

                "ranziz",

                "project",

                "ai"

            ]

        ):

            return 9



        if any(

            word in name

            for word in [

                "favorite",

                "warna",

                "genre"

            ]

        ):

            return 8



        return 5



    def rank(

        self,

        memories

    ):

        result = {}


        for key, value in memories.items():

            category = None


            if isinstance(value, dict):

                category = value.get(
                    "category"
                )


            result[key] = self.calculate(

                key,

                category

            )


        return dict(

            sorted(

                result.items(),

                key=lambda x: x[1],

                reverse=True

            )

        )



    def __repr__(self):

        return "MemoryPriority()"