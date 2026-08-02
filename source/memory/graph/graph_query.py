"""
RanZiz AI Graph Query
Version 1.0
"""


class GraphQuery:


    def related(

        self,

        graph,

        key

    ):

        node = graph.get(key)

        if node is None:

            return {}

        result = {}

        for neighbor in node.get(

            "links",

            []

        ):

            result[neighbor] = graph.get(

                neighbor,

                {}

            )

        return result


    def category(

        self,

        graph,

        category

    ):

        result = {}

        for key, node in graph.items():

            memory = node.get(

                "memory",

                {}

            )

            if memory.get(

                "category",

                ""

            ) == category:

                result[key] = node

        return result


    def search_value(

        self,

        graph,

        keyword

    ):

        keyword = keyword.lower()

        result = {}

        for key, node in graph.items():

            memory = node.get(

                "memory",

                {}

            )

            value = str(

                memory.get(

                    "value",

                    ""

                )

            ).lower()

            if keyword in value:

                result[key] = node

        return result


    def __repr__(self):

        return "GraphQuery()"