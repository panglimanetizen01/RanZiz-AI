"""
RanZiz AI Vision Engine
Version 1.0
"""

from source.engines.base_engine import BaseEngine


class VisionEngine(BaseEngine):

    NAME = "VisionEngine"

    def run(self, project, request):

        return {
            "type": "vision",
            "image": request.get(
                "image"
            ),
            "analysis": "READY",
            "status": "READY"
        }
