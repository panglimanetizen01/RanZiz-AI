"""
RanZiz AI Task Generator
Version 1.0
"""


class TaskGenerator:

    def generate(self, workflow):

        tasks = []

        for index, step in enumerate(workflow, start=1):

            tasks.append({

                "id": index,

                "name": step,

                "status": "PENDING"

            })

        return tasks