"""
RanZiz AI Task Executor
Version 2.0
"""

from source.capability.capability_executor import CapabilityExecutor
from source.capability.capability_loader import CapabilityLoader
from source.capability.capability_registry import CapabilityRegistry
from source.tasks.task import Task


class TaskExecutor:


    def __init__(self):

        self.registry = CapabilityRegistry()

        self.load_capabilities()

        self.executor = CapabilityExecutor(
            self.registry
        )


    def load_capabilities(self):

        loader = CapabilityLoader()

        capabilities = loader.load()


        for name, executor in capabilities.items():

            self.registry.register(
                name,
                executor
            )


    def execute(self, task):

        if not isinstance(task, Task):

            raise TypeError(
                "task harus berupa Task"
            )


        return self.executor.execute(
            task
        )