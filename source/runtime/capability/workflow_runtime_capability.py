"""
RanZiz AI Workflow Runtime Capability
Version 1.0
"""


class WorkflowRuntimeCapability:


    def __init__(

        self,

        workflow=None

    ):

        self.workflow = workflow


    def bind(

        self,

        workflow

    ):

        self.workflow = workflow

        return self


    def execute(

        self,

        message,

        context=None

    ):

        if self.workflow is None:

            return None


        if hasattr(

            self.workflow,

            "execute"

        ):

            return self.workflow.execute(

                message,

                context

            )


        return None