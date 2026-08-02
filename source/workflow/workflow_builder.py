"""
RanZiz AI Workflow Builder
Version 1.0
"""

from source.workflow.workflow import Workflow


class WorkflowBuilder:


    def build(self, name, tasks):

        workflow = Workflow(
            name=name,
            tasks=tasks
        )

        return workflow