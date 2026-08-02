"""
RanZiz AI Runtime Adapter
Version 1.0
"""

from source.planner.planner_runtime import PlannerRuntime


class RuntimeAdapter:

    def __init__(

        self,

        capability_executor

    ):

        self.runtime = PlannerRuntime(

            capability_executor

        )

    def execute(

        self,

        message,

        context=None

    ):

        return self.runtime.execute(

            message,

            context
        )