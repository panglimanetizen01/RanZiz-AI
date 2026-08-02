"""
RanZiz AI Capability Result
Version 1.0
"""


class CapabilityResult:


    def __init__(
        self,
        capability,
        status="SUCCESS",
        output=None,
        metadata=None
    ):

        self.capability = capability

        self.status = status

        self.output = output

        self.metadata = metadata or {}


    def to_dict(self):

        return {

            "capability": self.capability,

            "status": self.status,

            "output": self.output,

            "metadata": self.metadata

        }


    def __repr__(self):

        return (
            f"CapabilityResult("
            f"{self.capability}, "
            f"{self.status})"
        )