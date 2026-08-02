"""
RanZiz AI Runtime Facade
Version 1.0
"""


class RuntimeFacade:


    def __init__(

        self,

        kernel

    ):

        self.kernel = kernel



    def start(

        self,

        container

    ):

        return self.kernel.start(

            container

        )



    def chat(

        self,

        message,

        context=None

    ):

        return self.kernel.process(

            message,

            context

        )



    def stop(

        self

    ):

        return self.kernel.stop()