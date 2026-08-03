"""
RanZiz AI Workflow Builder
Version 1.0
"""


class WorkflowBuilder:

    def build(self, goal):

        workflows = {

            "MUSIC": [
                "Generate Lyrics",
                "Generate Melody",
                "Arrange Music",
                "Generate Vocal",
                "Mix & Master",
                "Export MP3"
            ],

            "VIDEO": [
                "Generate Script",
                "Generate Images",
                "Generate Voice",
                "Compose Video",
                "Render MP4"
            ],

            "IMAGE": [
                "Generate Image",
                "Upscale Image",
                "Export PNG"
            ],

            "WEBSITE": [
                "Generate Source",
                "Generate Assets",
                "Export Project"
            ],

            "APPLICATION": [
                "Generate Code",
                "Generate Project",
                "Export Source"
            ]

        }

        return workflows.get(goal, [])