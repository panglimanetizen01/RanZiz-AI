"""
RanZiz AI Memory Context Provider
Version 1.0
"""

from source.memory.context.context_builder import ContextBuilder


class MemoryContextProvider:


    def __init__(self):

        self.builder = ContextBuilder()


    def get_context(

        self,

        key

    ):

        return self.builder.build(

            key

        )


    def get_identity_context(

        self

    ):

        return self.builder.build(

            "nama"

        )


    def __repr__(self):

        return "MemoryContextProvider()"