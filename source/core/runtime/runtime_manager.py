"""
RanZiz AI Core Runtime Manager
Version 1.0
"""


from source.core.runtime.core_runtime_adapter import CoreRuntimeAdapter


class RuntimeManager:


    def __init__(

        self

    ):

        self.adapter = CoreRuntimeAdapter()



    def process(

        self,

        message,

        context=None

    ):

        return self.adapter.process(

            message,

            context

        )



    def start(

        self,

        container

    ):

        return self.adapter.start(

            container

        )



    def stop(

        self

    ):

        return self.adapter.stop()