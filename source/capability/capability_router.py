"""
RanZiz AI Capability Router
Version 2.0
"""

from source.capability.capability_loader import CapabilityLoader
from source.capability.capability_registry import CapabilityRegistry


class CapabilityRouter:

    def __init__(self):

        self.loader = CapabilityLoader()

        self.registry = CapabilityRegistry()

        self.load()


    def load(self):

        executors = self.loader.load()

        for name, executor in executors.items():

            self.registry.register(
                name,
                executor
            )


    def resolve(
        self,
        capabilities
    ):

        results = []

        for capability in capabilities:

            executor = self.registry.get(
                capability
            )

            if executor is not None:

                results.append(
                    executor
                )

        return results


    def available(self):

        return self.registry.list()


    def info(
        self,
        capability
    ):

        return self.registry.info(
            capability
        )


    def count(self):

        return self.registry.count()


    def __repr__(self):

        return (
            f"CapabilityRouter("
            f"{self.count()} capabilities)"
        )
