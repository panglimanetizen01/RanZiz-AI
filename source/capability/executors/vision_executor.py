"""
RanZiz AI Vision Executor
Version 1.0
"""

from source.capability.base_executor import BaseCapabilityExecutor
from source.capability.schema.capability_info import CapabilityInfo
from source.engines.vision.vision_engine import VisionEngine


class VisionExecutor(BaseCapabilityExecutor):

    def __init__(self):

        self.engine = VisionEngine()

    def execute(self, payload):

        return self.engine.run(
            None,
            payload
        )

    def metadata(self):

        return CapabilityInfo(

            name="Vision Engine",

            category="Vision",

            description="Image understanding engine",

            inputs=["image"],

            outputs=["analysis"],

            requires=[],

            priority=10

        )
