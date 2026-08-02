"""
RanZiz AI Capability Pipeline
Version 2.1
"""

from source.capability.validation.capability_validator import CapabilityValidator
from source.tasks.task import Task


class CapabilityPipeline:

    def __init__(
        self,
        executor=None,
        validator=None
    ):

        self.executor = executor

        self.validator = (
            validator
            if validator
            else CapabilityValidator()
        )

    def execute(
        self,
        plan,
        payload
    ):

        # ==========================
        # Legacy mode
        # ==========================
        if isinstance(plan, list):

            if self.executor is None:

                raise ValueError(
                    "Legacy pipeline membutuhkan executor."
                )

            results = []

            for capability in plan:

                task = Task(
                    capability,
                    capability,
                    payload
                )

                results.append(
                    self.executor.execute(
                        task
                    )
                )

            return results

        # ==========================
        # New CapabilityPlan mode
        # ==========================
        if not self.validator.validate(plan):

            return []

        results = []

        for item in plan:

            executor = item["executor"]

            results.append(
                {
                    "capability": item["name"],
                    "result": executor.execute(
                        payload
                    )
                }
            )

        return results