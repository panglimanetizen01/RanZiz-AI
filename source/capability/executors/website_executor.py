"""
RanZiz AI Website Executor
Version 2.0
"""

from source.capability.base_executor import BaseCapabilityExecutor
from source.capability.schema.capability_info import CapabilityInfo
from source.engines.website.website_engine import WebsiteEngine


class WebsiteExecutor(BaseCapabilityExecutor):

    def __init__(self):

        self.engine = WebsiteEngine()


    def execute(self, payload):

        context = payload.get(
            "context",
            {}
        )

        request = {

            "title": payload.get(
                "message",
                "Website"
            ),

            "framework": "HTML",

            "assets": context.get(
                "Image Engine",
                {}
            )

        }

        return self.engine.run(
            None,
            request
        )


    def metadata(self):

        return CapabilityInfo(

            name="Website Engine",

            category="Website",

            description="Website generator",

            inputs=[
                "text",
                "assets"
            ],

            outputs=[
                "website"
            ],

            requires=[
                "Image Engine"
            ],

            priority=20

        )
