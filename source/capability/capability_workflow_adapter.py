"""
RanZiz AI Capability Workflow Adapter
Version 1.0
"""

from source.tasks.task import Task
from source.workflow.workflow import Workflow


class CapabilityWorkflowAdapter:


    def build(
        self,
        name,
        capability_plan,
        message
    ):

        workflow = Workflow(name)

        for item in capability_plan:

            workflow.add_task(

                Task(

                    name=item["name"],

                    capability=item["name"],

                    payload={
                        "message": message
                    }

                )

            )

        return workflow