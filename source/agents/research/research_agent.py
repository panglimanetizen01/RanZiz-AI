"""
RanZiz AI Research Agent
Version 1.0
"""


from source.capability.capability_runtime import CapabilityRuntime
from source.capability.capability_planner import CapabilityPlanner


class ResearchAgent:


    def __init__(self):

        self.name = "Research Agent"

        self.capability_planner = CapabilityPlanner()

        self.runtime = CapabilityRuntime()


    def can_handle(self, message):

        text = message.lower()

        keywords = [
            "cari",
            "riset",
            "penelitian",
            "sejarah",
            "informasi",
            "analisis"
        ]

        return any(
            word in text
            for word in keywords
        )


    def execute(

        self,

        message

    ):

        capabilities = [
            "Research Engine"
        ]

        plan = self.capability_planner.create(
            capabilities
        )

        payload = {
            "message": message,
            "context": {}
        }

        return self.runtime.execute(
            plan,
            payload
        )


    def info(self):

        return {

            "name": self.name,

            "category": "Research",

            "description": "Agent khusus riset dan analisis informasi"

        }