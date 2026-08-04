"""
RanZiz AI Pipeline Executor
Version 2.0
"""

from source.capability.capability_planner import CapabilityPlanner
from source.capability.pipeline.capability_pipeline import CapabilityPipeline


class PipelineExecutor:

    def __init__(
        self,
        capability_executor
    ):

        self.planner = CapabilityPlanner()

        self.pipeline = CapabilityPipeline(
            capability_executor
        )

    def execute(
        self,
        plan
    ):

        capabilities = plan.get(
            "capabilities",
            []
        )

        payload = {

            "message": plan.get(
                "message",
                plan.get(
                    "topic",
                    ""
                )
            ),

            "context": plan.get(
                "context",
                {}
            )

        }

        capability_plan = self.planner.create(
            capabilities
        )

        return self.pipeline.execute(
            capability_plan,
            payload
        )

    def __repr__(self):

        return "PipelineExecutor(v2)"
