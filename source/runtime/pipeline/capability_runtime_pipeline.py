"""
RanZiz AI Capability Runtime Pipeline
Version 2.0
"""

from source.capability.capability_planner import CapabilityPlanner
from source.capability.capability_runtime import CapabilityRuntime


class CapabilityRuntimePipeline:


    def __init__(
        self,
        capability_pipeline=None
    ):

        self.planner = CapabilityPlanner()

        self.runtime = CapabilityRuntime()

        self.pipeline = capability_pipeline



    def execute(
        self,
        plan,
        context=None
    ):

        if plan is None:

            return None


        capabilities = plan.get(
            "capabilities",
            []
        )


        capability_plan = self.planner.create(
            capabilities
        )


        payload = {

            "message": plan.get(
                "message",
                ""
            ),

            "context": context or {},

            "intent": plan.get(
                "intent"
            ),

            "goal": plan.get(
                "goal"
            ),

            "task_type": plan.get(
                "task_type"
            )

        }


        return self.runtime.execute(
            capability_plan,
            payload
        )
