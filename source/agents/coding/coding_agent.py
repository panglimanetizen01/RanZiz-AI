"""
RanZiz AI Coding Agent
Version 1.1
"""

from source.capability.capability_runtime import CapabilityRuntime
from source.capability.capability_planner import CapabilityPlanner


class CodingAgent:

    def __init__(self):

        self.name = "Coding Agent"

        self.capability_planner = CapabilityPlanner()

        self.runtime = CapabilityRuntime()

    def can_handle(self, message):

        text = message.lower()

        keywords = [
            "kode",
            "coding",
            "program",
            "python",
            "website",
            "aplikasi",
            "software"
        ]

        return any(
            word in text
            for word in keywords
        )

    def execute(

        self,

        message,

        context=None

    ):

        capabilities = [
            "Code Engine"
        ]

        plan = self.capability_planner.create(
            capabilities
        )

        payload = {
            "message": message,
            "context": context or {}
        }

        return self.runtime.execute(
            plan,
            payload
        )


    def info(self):

        return {
            "name": self.name,
            "category": "Coding",
            "description": "Agent khusus pemrograman dan pengembangan software"
        }