"""
RanZiz AI Research Agent
Version 1.0
"""


from source.workflow.workflow_orchestrator import WorkflowOrchestrator


class ResearchAgent:


    def __init__(self):

        self.name = "Research Agent"

        self.orchestrator = WorkflowOrchestrator()


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


    def execute(self, message):

        return self.orchestrator.run(
            message
        )


    def info(self):

        return {

            "name": self.name,

            "category": "Research",

            "description": "Agent khusus riset dan analisis informasi"

        }