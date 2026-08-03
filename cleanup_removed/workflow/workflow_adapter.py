"""
RanZiz AI Workflow Adapter
Version 1.0
"""

from source.workflow.workflow import Workflow


class WorkflowAdapter:


    def from_tasks(self, name, tasks):

        return Workflow(
            name=name,
            tasks=tasks
        )