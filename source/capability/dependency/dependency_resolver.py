"""
RanZiz AI Dependency Resolver
Compatibility Wrapper
Version 3.0
"""

from source.capability.capability_router import CapabilityRouter
from source.capability.dependency.capability_dependency_resolver import (
    CapabilityDependencyResolver,
)


class DependencyResolver:

    def __init__(self):

        router = CapabilityRouter()

        self.resolver = CapabilityDependencyResolver(
            router.registry
        )

    def resolve(
        self,
        capabilities
    ):

        return self.resolver.resolve(
            capabilities
        )

    def graph(self):

        return self.resolver.graph()

    def __repr__(self):

        return repr(
            self.resolver
        )
