"""
RanZiz AI Memory Runtime Capability
Version 1.0
"""


class MemoryRuntimeCapability:


    def __init__(

        self,

        memory=None

    ):

        self.memory = memory


    def bind(

        self,

        memory

    ):

        self.memory = memory

        return self


    def execute(

        self,

        message,

        context=None

    ):

        if self.memory is None:

            return None


        if hasattr(

            self.memory,

            "retrieve"

        ):

            return self.memory.retrieve(

                message

            )


        return None