"""
RanZiz AI Document Engine
Version 1.0
"""

from source.engines.base_engine import BaseEngine


class DocumentEngine(BaseEngine):

    NAME = "DocumentEngine"

    def run(self, project, request):

        return {
            "type": "document",
            "title": request.get(
                "title",
                "Untitled Document"
            ),
            "format": request.get(
                "format",
                "pdf"
            ),
            "status": "READY"
        }
