"""
RanZiz AI Capability Command
Version 1.0
"""


from source.capability.service.capability_service import CapabilityService


class CapabilityCommand:


    def __init__(self):

        self.service = CapabilityService()


    def execute(self, message):

        text = message.lower()


        keywords = [
            "kemampuan",
            "skill",
            "fitur",
            "bisa apa",
            "apa yang bisa"
        ]


        if any(
            word in text
            for word in keywords
        ):

            return self.service.text()


        return None
