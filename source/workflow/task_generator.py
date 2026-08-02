"""
RanZiz AI Task Generator
Version 2.0
"""

from source.tasks.task import Task


class TaskGenerator:

    def generate(self, plan, message):

        tasks = []

        capabilities = plan.get(
            "capabilities",
            []
        )

        context = dict(
            plan.get(
                "context",
                {}
            )
        )

        for capability in capabilities:

            tasks.append(
                Task(
                    name=capability,
                    capability=capability,
                    payload={
                        "message": message,
                        "context": dict(context)
                    }
                )
            )

        return tasks