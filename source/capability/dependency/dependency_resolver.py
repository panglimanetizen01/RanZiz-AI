"""
RanZiz AI Dependency Resolver
Version 2.0
"""

from source.capability.catalog.catalog_service import CatalogService


class DependencyResolver:


    def __init__(self):

        self.catalog = CatalogService()


    def resolve(self, capabilities):

        ordered = []

        visited = set()

        metadata = {}

        for item in self.catalog.list():

            metadata[item["name"]] = item


        for capability in capabilities:

            self._visit(
                capability,
                metadata,
                visited,
                ordered
            )


        return ordered


    def _visit(

        self,

        capability,

        metadata,

        visited,

        ordered

    ):

        if capability in visited:

            return


        visited.add(capability)


        info = metadata.get(capability)


        if info:

            for dependency in info.get(
                "requires",
                []
            ):

                self._visit(

                    dependency,

                    metadata,

                    visited,

                    ordered

                )


        if capability not in ordered:

            ordered.append(capability)