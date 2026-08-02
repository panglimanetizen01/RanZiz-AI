"""
RanZiz AI Brain Runtime
Version 1.0
"""


class BrainRuntime:


    def __init__(

        self,

        orchestrator

    ):

        self.orchestrator = orchestrator



    def process(

        self,

        message,

        context,

        plan=None

    ):

        return self.orchestrator.execute(

            message,

            context,

            plan

        )