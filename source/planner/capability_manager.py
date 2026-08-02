"""
RanZiz AI Capability Manager
Version 2.2
"""


class CapabilityManager:


    def get_capabilities(
        self,
        goal
    ):

        goal = str(goal).upper()


        capabilities = {

            "MUSIC": [
                "Lyric Engine",
                "Composer",
                "Audio Engine"
            ],

            "CODING": [
                "Code Engine"
            ],

            "APPLICATION": [
                "Code Engine"
            ],

            "WEBSITE": [
                "Code Engine"
            ],

            "RESEARCH": [
                "Research Engine"
            ],

            "IMAGE": [
                "Image Engine"
            ],

            "VIDEO": [
                "Image Engine"
            ]

        }


        return capabilities.get(
            goal,
            []
        )


    def __repr__(self):

        return "CapabilityManager()"
