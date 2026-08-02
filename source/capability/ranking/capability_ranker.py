"""
RanZiz AI Capability Ranker
Version 3.0
"""

from source.capability.catalog.catalog_service import CatalogService


class CapabilityRanker:


    def __init__(
        self,
        catalog=None
    ):

        self.catalog = (
            catalog
            if catalog
            else CatalogService()
        )


    def rank(
        self,
        capabilities
    ):

        metadata = {
            item["name"]: item
            for item in self.catalog.list()
        }


        ordered = []


        def add(
            capability,
            stack=None
        ):

            if stack is None:
                stack = set()


            if capability in ordered:
                return


            if capability in stack:
                return


            stack.add(
                capability
            )


            info = metadata.get(
                capability,
                {}
            )


            for dependency in info.get(
                "requires",
                []
            ):

                add(
                    dependency,
                    stack
                )


            if capability not in ordered:

                ordered.append(
                    capability
                )


        for capability in capabilities:

            add(
                capability
            )


        return ordered