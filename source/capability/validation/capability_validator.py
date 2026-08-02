"""
RanZiz AI Capability Validator
Version 2.0
"""


class CapabilityValidator:


    def validate(
        self,
        plan
    ):

        if not hasattr(
            plan,
            "items"
        ):

            return False


        for item in plan.items:

            if "name" not in item:

                return False


            if "executor" not in item:

                return False


            executor = item["executor"]


            if executor is None:

                return False


        return True