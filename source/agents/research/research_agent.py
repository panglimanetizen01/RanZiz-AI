"""
RanZiz AI Research Agent
Version 2.0
"""


class ResearchAgent:


    def __init__(self):

        self.name = "research"


    def can_handle(
        self,
        message
    ):

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


    def create_task(
        self,
        message,
        context=None
    ):

        return {
            "capability": "Research Engine",
            "message": message,
            "context": context or {}
        }


    def info(self):

        return {
            "name": self.name,
            "display_name": "Research Agent",
            "category": "Research",
            "description": "Agent khusus riset dan analisis informasi"
        }
