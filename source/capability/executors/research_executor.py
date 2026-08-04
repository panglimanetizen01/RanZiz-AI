"""
RanZiz AI Research Executor
Version 1.0
"""

from source.capability.base_executor import BaseCapabilityExecutor
from source.capability.schema.capability_info import CapabilityInfo


class ResearchExecutor(BaseCapabilityExecutor):

    def execute(self, payload):

        message = payload.get(
            "message",
            ""
        )

        return self.success(
            {
                "topic": message,

                "status": "Research preparation ready"
            }
        )


    def metadata(self):

        return CapabilityInfo(

            name="Research Engine",

            category="Research",

            description="Melakukan analisis dan riset berdasarkan topik",

            inputs=[
                "text"
            ],

            outputs=[
                "research"
            ],

            requires=[],

            priority=10

        )
