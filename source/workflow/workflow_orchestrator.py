"""
RanZiz AI Workflow Orchestrator
Version 2.2
"""


from source.workflow.workflow_planner import WorkflowPlanner
from source.workflow.workflow_service import WorkflowService


class WorkflowOrchestrator:



    def __init__(

        self,

        executor=None

    ):

        self.planner = WorkflowPlanner()

        self.service = WorkflowService(
            executor
        )



    def create(

        self,

        message,

        context=None

    ):


        tasks = self.planner.create_tasks(
            message
        )


        workflow = self.service.create(
            "Auto Workflow",
            tasks,
            context
        )


        return workflow



    def run(

        self,

        message,

        context=None

    ):


        workflow = self.create(

            message,

            context

        )


        return self.service.run(

            workflow.name,

            context

        )