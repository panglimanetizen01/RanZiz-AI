"""
RanZiz AI Website Engine
Version 1.0
"""

from source.engines.base_engine import BaseEngine


class WebsiteEngine(BaseEngine):

    NAME = "WebsiteEngine"

    def run(self, project, request):

        return {
            "type": "website",
            "title": request.get(
                "title",
                "Untitled Website"
            ),
            "framework": request.get(
                "framework",
                "HTML"
            ),
            "pages": request.get(
                "pages",
                [
                    "Home"
                ]
            ),
            "status": "READY"
        }
