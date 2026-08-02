"""
RanZiz AI Knowledge Graph
Version 1.0
"""

from source.memory.relationship.memory_relationship import MemoryRelationship


class KnowledgeGraph:


    def __init__(self):

        self.relationship = MemoryRelationship()


    def build(

        self,

        memories

    ):

        relationships = self.relationship.build(

            memories

        )

        graph = {}


        for key, value in memories.items():

            if isinstance(value, dict):

                graph[key] = {

                    "memory": value,

                    "links": relationships.get(

                        key,

                        []

                    )

                }

            else:

                graph[key] = {

                    "memory": {

                        "value": value

                    },

                    "links": []

                }


        return graph


    def neighbors(

        self,

        graph,

        key

    ):

        node = graph.get(

            key

        )

        if node is None:

            return []

        return node.get(

            "links",

            []

        )


    def __repr__(self):

        return "KnowledgeGraph()"