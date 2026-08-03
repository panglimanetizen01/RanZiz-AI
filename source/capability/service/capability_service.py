"""
RanZiz AI Capability Service
Version 2.0
"""

from collections import defaultdict

from source.capability.capability_loader import CapabilityLoader
from source.capability.capability_registry import CapabilityRegistry
from source.capability.catalog.capability_catalog import CapabilityCatalog


class CapabilityService:

    def __init__(self):

        self.registry = CapabilityRegistry()

        self.catalog = CapabilityCatalog()

        self.load()


    def load(self):

        loader = CapabilityLoader()

        capabilities = loader.load()

        for name, executor in capabilities.items():

            self.registry.register(
                name,
                executor
            )

        self.catalog.add_many(
            self.registry.executors.values()
        )


    def get(
        self,
        name
    ):

        return self.registry.get(
            name
        )


    def info(
        self,
        name
    ):

        return self.registry.info(
            name
        )


    def count(self):

        return self.registry.count()


    def all(self):

        return self.catalog.list()


    def summary(self):

        capabilities = self.catalog.list()

        return {
            "count": len(capabilities),
            "capabilities": capabilities
        }


    def describe(self):

        return self.summary()["capabilities"]


    def text(self):

        summary = self.summary()

        groups = defaultdict(list)

        for item in summary["capabilities"]:

            groups[item["category"]].append(
                item
            )


        lines = []

        lines.append(
            f"RanZiz AI memiliki {summary['count']} capability.\n"
        )


        for category in sorted(groups):

            lines.append(
                f"\n[{category}]"
            )


            for item in sorted(
                groups[category],
                key=lambda x: x["priority"]
            ):

                lines.append(
                    f"• {item['name']}"
                )

                lines.append(
                    f"  {item['description']}"
                )


        return "\n".join(lines)


    def __repr__(self):

        return (
            f"CapabilityService("
            f"{self.count()} capabilities)"
        )
