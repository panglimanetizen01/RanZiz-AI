"""
RanZiz AI Runtime Bootstrap
Version 1.0
"""


from source.runtime.factory.runtime_factory import RuntimeFactory


class RuntimeBootstrap:


    def __init__(

        self,

        context_pipeline,

        decision_pipeline,

        memory_pipeline,

        capability_pipeline

    ):

        self.runtime = RuntimeFactory.create(

            context_pipeline,

            decision_pipeline,

            memory_pipeline,

            capability_pipeline

        )


    def get_runtime(self):

        return self.runtime