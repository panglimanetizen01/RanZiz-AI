"""
RanZiz AI Runtime Factory
Version 2.0
"""

from source.runtime.brain_runtime import BrainRuntime
from source.runtime.orchestrator.runtime_orchestrator import RuntimeOrchestrator


class RuntimeFactory:


    @staticmethod
    def create(

        context_pipeline,

        decision_pipeline,

        memory_pipeline,

    ):


        orchestrator = RuntimeOrchestrator(

            context_pipeline,

            decision_pipeline,

            memory_pipeline

        )


        return BrainRuntime(

            orchestrator

        )
