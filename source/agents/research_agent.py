"""
RanZiz AI Research Agent
Version 1.0
"""

from source.agents.base_agent import BaseAgent
from source.engine.ai_engine import AIEngine


class ResearchAgent(BaseAgent):

    @property
    def name(self):

        return "research"

    def __init__(self):

        self.engine = AIEngine()

    def can_handle(self, message):

        text = message.lower()

        keywords = (
            "apa",
            "siapa",
            "mengapa",
            "kenapa",
            "bagaimana",
            "kapan",
            "dimana",
            "di mana",
            "jelaskan",
            "explain"
        )

        return any(keyword in text for keyword in keywords)

    def execute(self, message):

        return self.engine.ask(message)