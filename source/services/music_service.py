"""
RanZiz AI Music Service
Version 1.0
"""

from source.engines.music.music_engine import MusicEngine
from source.parser.music_request_parser import MusicRequestParser


class MusicService:

    def __init__(self):

        self.engine = MusicEngine()

        self.parser = MusicRequestParser()

    def handle(self, message):

        request = self.parser.parse(message)

        result = self.engine.run(
            None,
            request
        )

        return result