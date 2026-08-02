"""
RanZiz AI Runtime Provider
Version 1.0
"""


from source.runtime.builder.runtime_builder import RuntimeBuilder


class RuntimeProvider:


    def __init__(

        self,

    ):

        self.builder = RuntimeBuilder()

        self.runtime = None



    def get(

        self

    ):

        if self.runtime is None:

            self.runtime = self.builder.build()


        return self.runtime



    def reset(

        self

    ):

        self.runtime = None