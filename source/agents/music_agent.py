"""
RanZiz AI Music Agent
Version 2.0
"""

from source.agents.base_agent import BaseAgent
from source.engines.music.music_engine import MusicEngine


class MusicAgent(BaseAgent):

    name = "music"

    KEYWORDS = (
        "lagu",
        "musik",
        "music",
        "dangdut",
        "pop",
        "rock",
        "jazz",
        "hip hop",
        "hiphop",
        "rap",
        "metal",
        "lirik",
        "lyric",
        "chorus",
        "verse",
        "melodi",
        "melody",
    )

    def __init__(self):

        self.engine = MusicEngine()

    def can_handle(self, message):

        if not isinstance(message, str):

            return False

        text = message.lower()

        return any(keyword in text for keyword in self.KEYWORDS)

    def execute(self, message):

        return self.engine.generate(message)