"""
RanZiz AI Music Agent
Version 2.0
"""

from source.agents.base_agent import BaseAgent
from source.capability.capability_runtime import CapabilityRuntime
from source.capability.capability_planner import CapabilityPlanner


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

        self.capability_planner = CapabilityPlanner()

        self.runtime = CapabilityRuntime()

    def can_handle(self, message):

        if not isinstance(message, str):

            return False

        text = message.lower()

        return any(keyword in text for keyword in self.KEYWORDS)

    def execute(self, message):

        capabilities = [
            "Lyric Engine",
            "Composer",
            "Audio Engine"
        ]

        plan = self.capability_planner.create(
            capabilities
        )

        payload = {
            "message": message,
            "context": {}
        }

        return self.runtime.execute(
            plan,
            payload
        )
