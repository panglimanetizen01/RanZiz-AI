"""
RanZiz AI Runtime Entry
Version 1.0
"""


from source.core.runtime.runtime_manager import RuntimeManager


class RuntimeEntry:


    def __init__(

        self

    ):

        self.manager = RuntimeManager()



    def execute(

        self,

        message,

        context=None

    ):

        return self.manager.process(

            message,

            context

        )



    def start(

        self,

        container

    ):

        return self.manager.start(

            container

        )



    def stop(

        self

    ):

        return self.manager.stop()