"""
RanZiz AI Audio Executor
Version 3.1
"""

from source.capability.base_executor import BaseCapabilityExecutor
from source.capability.schema.capability_info import CapabilityInfo
from source.parser.music_request_parser import MusicRequestParser


class AudioExecutor(BaseCapabilityExecutor):


    def __init__(self):

        self.parser = MusicRequestParser()


    def execute(self, payload):

        message = payload.get(
            "message",
            ""
        )

        request = self.parser.parse(
            message
        )

        context = payload.get(
            "context",
            {}
        )


        topic = (
            context.get("topic_detail")
            or request.get("topic", "")
        )


        emotion = (
            context.get("emotion")
            or request.get("emotion", "")
        )


        return self.success(
            {
                "genre": request.get(
                    "genre",
                    ""
                ),

                "topic": topic,

                "emotion": emotion,

                "status": "Audio preparation ready"
            }
        )


    def metadata(self):

        return CapabilityInfo(

            name="Audio Engine",

            category="Music",

            description="Menyiapkan proses audio generation",

            inputs=[
                "composition"
            ],

            outputs=[
                "audio"
            ],

            requires=[
                "Composer"
            ],

            priority=30

        )