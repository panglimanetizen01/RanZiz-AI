"""
RanZiz AI Task Builder
Version 1.1
"""

from source.tasks.task import Task


class TaskBuilder:


    def build(
        self,
        task_data
    ):

        if not isinstance(
            task_data,
            dict
        ):
            raise TypeError(
                "task_data harus berupa dictionary"
            )


        capabilities = task_data.get(
            "capabilities",
            []
        )

        if not capabilities:

            nested = task_data.get(
                "decision",
                {}
            )

            capabilities = nested.get(
                "capabilities",
                []
            )

        if capabilities:

            capability = capabilities[0]

        else:

            capability = task_data.get(
                "capability",
                "chat"
            )


        message = task_data.get(
            "message",
            ""
        )

        context = task_data.get(
            "context",
            {}
        )


        return Task(
            name=f"{capability}_task",
            capability=capability,
            payload={
                "message": message,
                "context": context,
                "capabilities": capabilities
            }
        )
