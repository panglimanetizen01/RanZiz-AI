"""
RanZiz AI Runtime Orchestrator
Version 2.0
"""


class RuntimeOrchestrator:

    def __init__(
        self,
        context_pipeline,
        decision_pipeline,
        memory_pipeline
    ):

        from source.tasks.task_builder import TaskBuilder
        from source.tasks.task_executor import TaskExecutor

        self.context = context_pipeline
        self.decision = decision_pipeline
        self.memory = memory_pipeline

        self.task_builder = TaskBuilder()
        self.task_executor = TaskExecutor()


    def execute(
        self,
        message,
        request_context,
        plan=None
    ):

        self.context.execute(
            request_context,
            message
        )

        decision_result = self.decision.execute(
            message,
            request_context
        )

        learned = self.memory.execute(
            message,
            decision_result
        )

        if learned is not None:
            return learned


        if decision_result is not None:

            if hasattr(
                decision_result,
                "to_dict"
            ):
                decision_result = decision_result.to_dict()

            elif isinstance(
                decision_result,
                dict
            ):

                nested = decision_result.get(
                    "decision"
                )

                if hasattr(
                    nested,
                    "to_dict"
                ):
                    decision_result["decision"] = nested.to_dict()

            task = self.task_builder.build(
                decision_result
            )

            if task is not None:
                return self.task_executor.execute(
                    task
                )


        return decision_result
