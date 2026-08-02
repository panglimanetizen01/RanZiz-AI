"""
RanZiz AI Capability Router
Version 1.0
"""

from source.capability.capability_loader import CapabilityLoader


class CapabilityRouter:


    def __init__(self):

        self.loader = CapabilityLoader()

        self.executors = self.loader.load()


    def resolve(self, capabilities):

        results = []

        for capability in capabilities:

            executor = self.executors.get(
                capability
            )

            if executor is not None:

                results.append(
                    executor
                )

        return results


    def available(self):

        return list(
            self.executors.keys()
        )