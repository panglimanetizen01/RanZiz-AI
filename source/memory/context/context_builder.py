"""
RanZiz AI Context Builder
Version 1.0
"""

from source.memory.graph.knowledge_graph import KnowledgeGraph
from source.memory.memory_repository import MemoryRepository
from source.memory.migration.memory_migration import MemoryMigration
from source.memory.reasoning.memory_reasoner import MemoryReasoner


class ContextBuilder:


    def __init__(self):

        self.repository = MemoryRepository()

        self.migration = MemoryMigration()

        self.graph = KnowledgeGraph()

        self.reasoner = MemoryReasoner()


    def build(

        self,

        key

    ):

        memories = self.migration.migrate(

            self.repository.all()

        )

        graph = self.graph.build(

            memories

        )

        return self.reasoner.summarize(

            graph,

            key

        )


    def __repr__(self):

        return "ContextBuilder()"