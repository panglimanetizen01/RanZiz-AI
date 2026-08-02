"""
RanZiz AI Runtime Bootstrap
Version 2.0
"""


from source.runtime.builder.runtime_builder import RuntimeBuilder


class RuntimeBootstrap:


    def __init__(

        self,

        context_pipeline=None,

        decision_pipeline=None,

        memory_pipeline=None,

        capability_pipeline=None

    ):

        self.builder = RuntimeBuilder()

        self.runtime = self.builder.build()



    def get_runtime(self):

        return self.runtime
