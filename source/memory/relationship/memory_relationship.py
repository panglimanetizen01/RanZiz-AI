"""
RanZiz AI Memory Relationship
Version 1.0
"""


class MemoryRelationship:


    def build(

        self,

        memories

    ):

        relationships = {}

        keys = list(memories.keys())


        for key in keys:

            relationships[key] = []


        for key in keys:

            item = memories[key]

            if not isinstance(item, dict):

                continue


            category = item.get(

                "category",

                ""

            )


            for other in keys:

                if other == key:

                    continue


                other_item = memories[other]

                if not isinstance(

                    other_item,

                    dict

                ):

                    continue


                if other_item.get(

                    "category",

                    ""

                ) == category:

                    relationships[key].append(

                        other

                    )


        return relationships


    def __repr__(self):

        return "MemoryRelationship()"