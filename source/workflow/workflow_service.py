"""
RanZiz AI Workflow Service
Version 1.1
"""


from source.workflow.workflow_builder import WorkflowBuilder
from source.workflow.workflow_engine import WorkflowEngine
from source.workflow.workflow_registry import WorkflowRegistry
from source.workflow.workflow_runner import WorkflowRunner


class WorkflowService:



    def __init__(

        self,

        executor

    ):


        self.builder = WorkflowBuilder()


        self.registry = WorkflowRegistry()


        self.runner = WorkflowRunner(

            self.registry,

            WorkflowEngine(
                executor
            )

        )



    def create(

        self,

        name,

        tasks,

        context=None

    ):


        workflow = self.builder.build(

            name,

            tasks

        )


        self.registry.register(

            workflow

        )


        return workflow



    def run(

        self,

        name,

        context=None

    ):


        return self.runner.run(

            name,

            context

        )



    def list(self):


        return self.registry.list_workflows()