"""
RanZiz AI Runtime Container
Version 1.0
"""


class RuntimeContainer:


    def __init__(

        self,

        brain_runtime=None,

        runtime_adapter=None

    ):

        self.brain_runtime = brain_runtime

        self.runtime_adapter = runtime_adapter



    def set_brain_runtime(

        self,

        runtime

    ):

        self.brain_runtime = runtime



    def set_runtime_adapter(

        self,

        adapter

    ):

        self.runtime_adapter = adapter



    def get_brain_runtime(self):

        return self.brain_runtime



    def get_runtime_adapter(self):

        return self.runtime_adapter



    def ready(self):

        return (

            self.brain_runtime is not None

            and

            self.runtime_adapter is not None

        )