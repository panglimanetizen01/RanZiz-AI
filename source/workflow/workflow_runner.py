"""
RanZiz AI Workflow Runner
Version 1.1
"""


class WorkflowRunner:



    def __init__(

        self,

        registry,

        engine

    ):


        self.registry = registry

        self.engine = engine



    def run(

        self,

        workflow_name,

        context=None

    ):


        workflow = self.registry.get(

            workflow_name

        )


        if workflow is None:

            return None



        return self.engine.run(

            workflow,

            context

        )