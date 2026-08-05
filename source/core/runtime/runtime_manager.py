"""
RanZiz AI Core Runtime Manager
Version 3.0
"""

from source.runtime.builder.runtime_builder import RuntimeBuilder


class RuntimeManager:


    def __init__(self):

        self.bridge = RuntimeBuilder().build()


    def process(
        self,
        message,
        context=None
    ):

        return self.bridge.process(
            message,
            context
        )

    def execute(
        self,
        message,
        context=None
    ):

        return self.process(
            message,
            context
        )



    def start(
        self,
        container
    ):

        return self.bridge.start(
            container
        )


    def stop(
        self
    ):

        return self.bridge.stop()
