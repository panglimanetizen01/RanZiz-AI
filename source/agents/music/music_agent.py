"""
RanZiz AI Music Agent
Version 1.2
"""

from source.workflow.workflow_orchestrator import WorkflowOrchestrator


class MusicAgent:


    def __init__(self):

        self.name = "Music Agent"

        self.orchestrator = WorkflowOrchestrator()



    def can_handle(
        self,
        message
    ):

        if not isinstance(
            message,
            str
        ):
            return False


        text = message.lower()


        keywords = (
            "lagu",
            "musik",
            "lirik",
            "dangdut",
            "pop",
            "rock"
        )


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
            "category": "Music",
            "description": "Agent khusus pembuatan musik dan lirik"
        }
