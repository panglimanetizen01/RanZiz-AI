"""
RanZiz AI Lyric Executor
Version 3.0
"""

from source.capability.base_executor import BaseCapabilityExecutor
from source.capability.schema.capability_info import CapabilityInfo
from source.engines.music.music_engine import MusicEngine
from source.parser.music_request_parser import MusicRequestParser


class LyricExecutor(BaseCapabilityExecutor):


    def __init__(self):

        self.engine = MusicEngine()

        self.parser = MusicRequestParser()


    def execute(self, payload):

        message = payload.get(
            "message",
            ""
        )

        request = self.parser.parse(
            message
        )

        result = self.engine.run(
            None,
            request
        )

        return result.get(
            "lyrics",
            ""
        )


    def metadata(self):

        return CapabilityInfo(

            name="Lyric Engine",

            category="Music",

            description="Membuat lirik lagu berdasarkan tema dan genre",

            inputs=[
                "text"
            ],

            outputs=[
                "lyrics"
            ],

            requires=[],

            priority=10

        )