"""
RanZiz AI Capability Catalog Service
Version 1.2
"""

from source.capability.capability_loader import CapabilityLoader
from source.capability.catalog.capability_catalog import CapabilityCatalog


class CatalogService:

    def __init__(self):

        self.catalog = CapabilityCatalog()

        self.load()

    def load(self):

        loader = CapabilityLoader()

        executors = loader.load()

        self.catalog.add_many(
            executors.values()
        )

    def list(self):

        return self.catalog.list()

    def find(
        self,
        keyword
    ):

        return self.catalog.search(
            keyword
        )

    def summary(self):

        capabilities = self.catalog.list()

        return {
            "count": len(capabilities),
            "capabilities": capabilities
        }