"""
RanZiz AI Voice Executor
Version 2.0
"""

from source.capability.base_executor import BaseCapabilityExecutor
from source.capability.schema.capability_info import CapabilityInfo
from source.engines.voice.voice_engine import VoiceEngine


class VoiceExecutor(BaseCapabilityExecutor):

    def __init__(self):

        self.engine = VoiceEngine()


    def execute(self, payload):

        context = payload.get(
            "context",
            {}
        )

        text = payload.get(
            "message",
            ""
        )

        document = context.get(
            "Document Engine",
            {}
        )

        if document:

            text = str(document)


        return self.engine.run(
            None,
            {
                "text": text
            }
        )


    def metadata(self):

        return CapabilityInfo(

            name="Voice Engine",

            category="Voice",

            description="Voice synthesis engine",

            inputs=[
                "text",
                "document"
            ],

            outputs=[
                "voice"
            ],

            requires=[
                "Document Engine"
            ],

            priority=30

        )
