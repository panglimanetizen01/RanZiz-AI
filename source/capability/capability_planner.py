"""
RanZiz AI Capability Planner
Version 1.4
"""

from source.capability.capability_plan import CapabilityPlan
from source.capability.capability_router import CapabilityRouter
from source.capability.dependency.capability_dependency_resolver import (
    CapabilityDependencyResolver,
)
from source.capability.ranking.capability_ranker import CapabilityRanker


class CapabilityPlanner:

    def __init__(self):

        self.router = CapabilityRouter()

        self.ranker = CapabilityRanker()

        self.resolver = CapabilityDependencyResolver(
            self.router.registry
        )

    def create(
        self,
        capabilities
    ):

        plan = CapabilityPlan()

        ranked = self.ranker.rank(
            capabilities
        )

        resolved = self.resolver.resolve(
            ranked
        )

        executors = self.router.resolve(
            resolved
        )

        for executor in executors:

            info = executor.metadata().info()

            plan.add(
                info["name"],
                executor,
                info.get(
                    "requires",
                    []
                )
            )

        return plan

    def __repr__(self):

        return (
            f"CapabilityPlanner("
            f"{len(self.router.available())} capabilities)"
        )
