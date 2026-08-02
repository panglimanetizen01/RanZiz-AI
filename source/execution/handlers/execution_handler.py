"""
RanZiz AI Execution Handler
Version 3.0
"""


class ExecutionHandler:

    def __init__(
        self,
        planner,
        executor,
        runtime_handler
    ):

        self.planner = planner
        self.executor = executor
        self.runtime_handler = runtime_handler

    def execute(
        self,
        message,
        context,
        decision
    ):


        plan = self.planner.plan(
            message,
            context
        )

        result = self.executor.execute(
            plan
        )

        if result is not None:
            return result

        return self.runtime_handler.handle(
            message,
            decision
        )