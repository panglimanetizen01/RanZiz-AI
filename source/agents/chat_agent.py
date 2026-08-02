"""
RanZiz AI Chat Agent
Version 1.0
"""

from source.agents.base_agent import BaseAgent
from source.engine.ai_engine import AIEngine


class ChatAgent(BaseAgent):

    @property
    def name(self):

        return "chat"

    def __init__(self):

        self.ai = AIEngine()

    def can_handle(self, message):

        return True

    def execute(self, message):

        return self.ai.ask(message)