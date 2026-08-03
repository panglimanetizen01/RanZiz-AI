"""
RanZiz AI Document Executor
Version 2.0
"""

from source.capability.base_executor import BaseCapabilityExecutor
from source.capability.schema.capability_info import CapabilityInfo
from source.engines.document.document_engine import DocumentEngine


class DocumentExecutor(BaseCapabilityExecutor):

    def __init__(self):

        self.engine = DocumentEngine()


    def execute(self, payload):

        context = payload.get(
            "context",
            {}
        )

        request = {

            "title": payload.get(
                "message",
                "Document"
            ),

            "research": context.get(
                "Research Engine",
                {}
            )

        }

        return self.engine.run(
            None,
            request
        )


    def metadata(self):

        return CapabilityInfo(

            name="Document Engine",

            category="Document",

            description="Document generation engine",

            inputs=[
                "text",
                "research"
            ],

            outputs=[
                "document"
            ],

            requires=[
                "Research Engine"
            ],

            priority=20

        )
