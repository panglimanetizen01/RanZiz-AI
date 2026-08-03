"""
RanZiz AI Capability Registry
Version 2.0
"""

from source.capability.schema.capability_info import CapabilityInfo


class CapabilityRegistry:

    def __init__(self):
        self.executors = {}
        self.metadata = {}

    def register(
        self,
        name,
        executor,
        info=None
    ):
        self.executors[name] = executor

        if info is None:
            info = CapabilityInfo(
                name=name,
                category="general",
                description="",
                inputs=[],
                outputs=[]
            )

        self.metadata[name] = info

    def get(
        self,
        name
    ):
        return self.executors.get(name)

    def info(
        self,
        name
    ):
        capability = self.metadata.get(name)

        if capability is None:
            return None

        return capability.info()

    def all(self):
        return {
            name: self.metadata[name].info()
            for name in self.metadata
        }

    def list(self):
        return list(
            self.executors.keys()
        )

    def has(
        self,
        name
    ):
        return name in self.executors

    def remove(
        self,
        name
    ):
        self.executors.pop(
            name,
            None
        )

        self.metadata.pop(
            name,
            None
        )

    def count(self):
        return len(
            self.executors
        )


    def __repr__(self):
        return (
            f"CapabilityRegistry("
            f"{self.count()} capabilities)"
        )
