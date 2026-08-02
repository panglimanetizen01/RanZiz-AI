"""
RanZiz AI Capability Planner
Version 1.2
"""

from source.capability.capability_plan import CapabilityPlan
from source.capability.capability_router import CapabilityRouter
from source.capability.dependency.dependency_resolver import DependencyResolver
from source.capability.ranking.capability_ranker import CapabilityRanker


class CapabilityPlanner:


    def __init__(self):

        self.router = CapabilityRouter()

        self.ranker = CapabilityRanker()

        self.resolver = DependencyResolver()


    def create(
        self,
        capabilities
    ):

        plan = CapabilityPlan()


        ranked_capabilities = self.ranker.rank(
            capabilities
        )


        resolved_capabilities = self.resolver.resolve(
            ranked_capabilities
        )


        executors = self.router.resolve(
            resolved_capabilities
        )


        for executor in executors:

            plan.add(
                executor.metadata().info()["name"],
                executor
            )


        return plan