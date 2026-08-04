"""
RanZiz AI Image Executor
Version 1.0
"""

from source.capability.base_executor import BaseCapabilityExecutor
from source.capability.schema.capability_info import CapabilityInfo


class ImageExecutor(BaseCapabilityExecutor):

    def execute(self, payload):

        message = payload.get(
            "message",
            ""
        )

        return self.success(
            {
                "prompt": message,
                "status": "Image generation preparation ready"
            }
        )


    def metadata(self):

        return CapabilityInfo(

            name="Image Engine",

            category="Image",

            description="Membuat konsep dan proses image generation",

            inputs=[
                "text"
            ],

            outputs=[
                "image"
            ],

            requires=[],

            priority=10

        )
