"""
RanZiz AI Video Executor
Version 2.0
"""

from source.capability.base_executor import BaseCapabilityExecutor
from source.capability.schema.capability_info import CapabilityInfo
from source.engines.video.video_engine import VideoEngine


class VideoExecutor(BaseCapabilityExecutor):

    def __init__(self):

        self.engine = VideoEngine()


    def execute(self, payload):

        context = payload.get(
            "context",
            {}
        )

        request = {

            "title": payload.get(
                "message",
                "Video"
            ),

            "audio": context.get(
                "Audio Engine",
                {}
            ),

            "lyrics": context.get(
                "Lyric Engine",
                ""
            )

        }

        return self.engine.run(
            None,
            request
        )


    def metadata(self):

        return CapabilityInfo(

            name="Video Engine",

            category="Video",

            description="Video generation engine",

            inputs=[
                "text",
                "audio",
                "lyrics"
            ],

            outputs=[
                "video"
            ],

            requires=[
                "Audio Engine"
            ],

            priority=30

        )
