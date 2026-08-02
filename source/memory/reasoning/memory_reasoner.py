"""
RanZiz AI Memory Reasoner
Version 1.0
"""

from source.memory.graph.graph_query import GraphQuery


class MemoryReasoner:


    def __init__(self):

        self.query = GraphQuery()


    def summarize(

        self,

        graph,

        key

    ):

        node = graph.get(key)

        if node is None:

            return "Memory tidak ditemukan."

        memory = node["memory"]

        text = []

        text.append(

            f"{key} = {memory['value']}"

        )

        related = self.query.related(

            graph,

            key

        )

        for other, item in related.items():

            text.append(

                f"{other} = {item['memory']['value']}"

            )

        return "\n".join(text)


    def __repr__(self):

        return "MemoryReasoner()"