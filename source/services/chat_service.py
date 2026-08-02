"""
RanZiz AI Chat Service
Version 1.0
"""

from source.engine.ai_engine import AIEngine


class ChatService:

    def __init__(self):

        self.ai = AIEngine()

    def handle(self, message):

        return self.ai.ask(message)