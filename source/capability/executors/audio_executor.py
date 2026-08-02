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

        return (
            "Audio Engine Result\n\n"
            f"Genre : {request.get('genre', '')}\n"
            f"Topic : {request.get('topic', '')}\n"
            f"Emotion : {request.get('emotion', '')}\n"
            "Status : Audio preparation ready"
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