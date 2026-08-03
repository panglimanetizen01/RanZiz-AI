"""
RanZiz AI Task Executor
Version 3.0
"""

from source.capability.capability_executor import CapabilityExecutor
from source.capability.capability_loader import CapabilityLoader
from source.capability.capability_registry import CapabilityRegistry
from source.tasks.task import Task


class TaskExecutor:


    def __init__(
        self,
        registry=None
    ):

        if registry is None:

            registry = CapabilityRegistry()

            self.load_capabilities(
                registry
            )


        self.registry = registry


        self.executor = CapabilityExecutor(
            self.registry
        )



    def load_capabilities(
        self,
        registry
    ):

        loader = CapabilityLoader()

        capabilities = loader.load_with_metadata()


        for name, item in capabilities.items():

            registry.register(

                name,

                item["executor"],

                item["info"]

            )



    def execute(
        self,
        task
    ):

        if not isinstance(
            task,
            Task
        ):

            raise TypeError(
                "task harus berupa Task"
            )


        return self.executor.execute(
            task
        )



    def available(self):

        return self.registry.list()



    def count(self):

        return self.registry.count()



    def __repr__(self):

        return (
            f"TaskExecutor("
            f"{self.count()} capabilities)"
        )
