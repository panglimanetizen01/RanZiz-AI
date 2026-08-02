"""
RanZiz AI Planner Runtime
Version 1.0
"""

from source.planner.pipeline_executor import PipelineExecutor
from source.planner.task_planner import TaskPlanner


class PlannerRuntime:


    def __init__(

        self,

        capability_executor

    ):

        self.planner = TaskPlanner()

        self.executor = PipelineExecutor(

            capability_executor

        )


    def execute(

        self,

        message,

        context=None

    ):

        plan = self.planner.plan(

            message,

            context or {}

        )

        return self.executor.execute(

            plan

        )