"""
RanZiz AI Workflow Engine
Version 2.0
"""

from source.capability.capability_registry import CapabilityRegistry
from source.capability.capability_router import CapabilityRouter


class WorkflowEngine:


    def __init__(
        self,
        registry=None
    ):

        if registry is None:

            self.router = CapabilityRouter()

            self.registry = self.router.registry

        else:

            self.registry = registry



    def available(self):

        return self.registry.list()



    def resolve(
        self,
        workflow
    ):

        result = []


        for item in workflow:

            executor = self.registry.get(
                item
            )


            if executor is not None:

                result.append(
                    executor
                )


        return result



    def execute(
        self,
        workflow,
        payload
    ):

        results = {}


        if hasattr(workflow, "tasks"):
            tasks = workflow.tasks
        else:
            tasks = workflow


        for name in tasks:

            executor = self.registry.get(
                name
            )


            if executor is None:

                results[name] = {
                    "error": "Capability tidak ditemukan"
                }

                continue


            try:

                results[name] = executor.execute(
                    payload
                )


            except Exception as error:  # noqa: BLE001

                results[name] = {
                    "error": str(error)
                }


        return results



    def run(
        self,
        workflow,
        context=None
    ):

        return self.execute(
            workflow,
            context
        )


    def count(self):

        return self.registry.count()



    def __repr__(self):

        return (
            f"WorkflowEngine("
            f"{self.count()} capabilities)"
        )
