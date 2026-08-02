"""
RanZiz AI Capability Service
Version 1.1
"""

from collections import defaultdict

from source.capability.catalog.catalog_service import CatalogService


class CapabilityService:

    def __init__(self):

        self.catalog = CatalogService()

    def all(self):

        return self.catalog.list()

    def summary(self):

        return self.catalog.summary()

    def describe(self):

        return self.summary()["capabilities"]

    def text(self):

        summary = self.summary()

        groups = defaultdict(list)

        for item in summary["capabilities"]:
            groups[item["category"]].append(item)

        lines = []

        lines.append(
            f"RanZiz AI memiliki {summary['count']} capability.\n"
        )

        for category in sorted(groups):

            lines.append(f"\n[{category}]")

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