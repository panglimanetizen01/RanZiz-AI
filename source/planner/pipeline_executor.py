"""
RanZiz AI Pipeline Executor
Version 1.0
"""

from source.capability.pipeline.capability_pipeline import CapabilityPipeline


class PipelineExecutor:

    def __init__(

        self,

        capability_executor

    ):

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

                "topic",

                ""

            )

        }

        return self.pipeline.execute(

            capabilities,

            payload

        )