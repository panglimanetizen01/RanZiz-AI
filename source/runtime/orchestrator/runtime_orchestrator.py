"""
RanZiz AI Runtime Orchestrator
Version 1.0
"""


class RuntimeOrchestrator:


    def __init__(

        self,

        context_pipeline,

        decision_pipeline,

        memory_pipeline,

        capability_pipeline

    ):

        self.context = context_pipeline

        self.decision = decision_pipeline

        self.memory = memory_pipeline

        self.capability = capability_pipeline



    def execute(

        self,

        message,

        request_context,

        plan=None

    ):

        self.context.execute(

            request_context,

            message

        )


        decision = self.decision.execute(

            message,

            request_context

        )


        learned = self.memory.execute(

            message,

            decision["decision"]

        )


        if learned is not None:

            return learned


        if plan is not None:

            return self.capability.execute(

                plan

            )


        return decision
