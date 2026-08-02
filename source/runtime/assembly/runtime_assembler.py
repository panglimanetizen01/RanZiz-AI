"""
RanZiz AI Runtime Assembler
Version 1.0
"""


from source.runtime.container.runtime_container import RuntimeContainer


class RuntimeAssembler:


    def assemble(

        self,

        brain_runtime=None,

        runtime_adapter=None

    ):

        container = RuntimeContainer(

            brain_runtime,

            runtime_adapter

        )


        return container