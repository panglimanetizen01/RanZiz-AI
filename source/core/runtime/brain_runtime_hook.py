"""
RanZiz AI Brain Runtime Hook
Version 1.0
"""


from source.core.runtime.runtime_entry import RuntimeEntry


class BrainRuntimeHook:


    def __init__(

        self

    ):

        self.runtime = RuntimeEntry()



    def execute(

        self,

        message,

        context=None

    ):

        return self.runtime.execute(

            message,

            context

        )