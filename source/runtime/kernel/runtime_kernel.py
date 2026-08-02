"""
RanZiz AI Runtime Kernel
Version 1.0
"""


class RuntimeKernel:


    def __init__(

        self,

        provider

    ):

        self.provider = provider



    def start(

        self,

        container

    ):

        runtime = self.provider.get()

        return runtime.start(

            container

        )



    def process(

        self,

        message,

        context=None

    ):

        runtime = self.provider.get()

        return runtime.process(

            message,

            context

        )



    def stop(

        self

    ):

        runtime = self.provider.get()

        return runtime.stop()