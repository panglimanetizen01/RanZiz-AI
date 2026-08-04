"""
RanZiz AI Executor
Version 3.0
"""

from datetime import UTC, datetime

from source.capability.capability_planner import CapabilityPlanner
from source.capability.capability_runtime import CapabilityRuntime


class Executor:


    def __init__(self):

        self.history = []

        self.capability_planner = CapabilityPlanner()

        self.capability_runtime = CapabilityRuntime()



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


        if capabilities:

            capability_plan = self.capability_planner.create(
                capabilities
            )


            result = self.capability_runtime.execute(
                capability_plan,
                payload
            )

        else:

            return None



        output = {

            "topic": plan.get(
                "topic"
            ),

            "intent": plan.get(
                "intent"
            ),

            "goal": plan.get(
                "goal"
            ),

            "task_type": plan.get(
                "task_type"
            ),

            "capabilities": capabilities,

            "result": result,

            "status": "SUCCESS",

            "timestamp": datetime.now(UTC).isoformat()

        }


        self.history.append(
            output
        )


        return output



    def last(
        self
    ):

        if not self.history:

            return None

        return self.history[-1]



    def clear(
        self
    ):

        self.history.clear()



    def all(
        self
    ):

        return list(
            self.history
        )