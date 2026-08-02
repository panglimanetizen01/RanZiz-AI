"""
RanZiz AI Workflow Planner
Version 3.1
"""

from source.planner.task_planner import TaskPlanner
from source.workflow.task_generator import TaskGenerator


class WorkflowPlanner:

    def __init__(self):

        self.planner = TaskPlanner()
        self.generator = TaskGenerator()

    def create_tasks(self, message):

        plan = self.get_plan(message)

        return self.generator.generate(
            plan,
            message
        )

    def get_plan(self, message):

        return self.planner.plan(message)