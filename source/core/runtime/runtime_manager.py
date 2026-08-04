"""
RanZiz AI Core Runtime Manager
Version 2.0
"""

from source.runtime.composition.runtime_composition_root import RuntimeCompositionRoot


class RuntimeManager:


    def __init__(
        self
    ):

        self.root = RuntimeCompositionRoot()

        self.runtime = self.root.get_runtime()


    def process(
        self,
        message,
        context=None
    ):

        return self.runtime.chat(
            message,
            context
        )


    def start(
        self,
        container
    ):

        return self.runtime.start(
            container
        )


    def stop(
        self
    ):

        return self.runtime.stop()
