"""
RanZiz AI Coding Agent
Version 1.1
"""

from source.workflow.workflow_orchestrator import WorkflowOrchestrator


class CodingAgent:

    def __init__(self):

        self.name = "Coding Agent"
        self.orchestrator = WorkflowOrchestrator()

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

        return self.orchestrator.run(

            message,

            context

        )

    def info(self):

        return {
            "name": self.name,
            "category": "Coding",
            "description": "Agent khusus pemrograman dan pengembangan software"
        }