"""
RanZiz AI Failure Test Capability
Version 1.0
"""


class FailureTestError(Exception):
    """Simulasi kegagalan permanen."""


class FailureTestCapability:

    def execute(self, payload):
        raise FailureTestError(
            "Simulasi gagal permanen"
        )