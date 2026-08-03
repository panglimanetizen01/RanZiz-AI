"""
RanZiz AI Pipeline Executor
Version 2.0
"""

from source.capability.pipeline.capability_pipeline import CapabilityPipeline


class PipelineExecutor:

    def __init__(self, capability_executor):

        self.pipeline = CapabilityPipeline(
            capability_executor
        )

    def execute(self, plan):

        payload = {

            "message": plan.get(
                "message",
                plan.get(
                    "topic",
                    ""
                )
            ),

            "topic": plan.get(
                "topic",
                ""
            ),

            "goal": plan.get(
                "goal",
                ""
            ),

            "intent": plan.get(
                "intent",
                ""
            ),

            "context": dict(
                plan.get(
                    "context",
                    {}
                )
            )

        }

        return self.pipeline.execute(

            plan.get(
                "capabilities",
                []
            ),

            payload

        )
