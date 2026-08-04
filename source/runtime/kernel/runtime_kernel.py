"""
RanZiz AI Runtime Kernel
Version 2.0
"""


class RuntimeKernel:


    def __init__(
        self,
        provider
    ):

        self.provider = provider

        self.runtime = self.provider.get()



    def get_runtime(
        self
    ):

        return self.runtime



    def start(
        self,
        container
    ):

        return self.runtime.start(
            container
        )



    def process(
        self,
        message,
        context=None
    ):

        return self.runtime.process(
            message,
            context
        )



    def stop(
        self
    ):

        return self.runtime.stop()



    def __repr__(self):

        return (
            f"RuntimeKernel("
            f"{self.runtime})"
        )
