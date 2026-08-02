"""
RanZiz AI AI Engine
Version 3.0
"""

from source.engine.provider_selector import ProviderSelector
from source.services.memory_service import MemoryService


class AIEngine:

    def __init__(self):

        self.selector = ProviderSelector()
        self.memory = MemoryService()

    def provider(self, capability="chat"):

        return self.selector.select(capability)

    def build_prompt(self, user_message):

        history = self.memory.last(5)

        prompt = "=== MEMORY ===\n"

        for item in history:

            if (
                isinstance(item, dict)
                and item.get("type") == "chat"
            ):

                user = item.get("user", "")
                assistant = item.get("assistant", "")

                prompt += (
                    f"User: {user}\n"
                    f"Assistant: {assistant}\n"
                )

        prompt += f"\n=== USER ===\n{user_message}"

        return prompt

    def ask(self, message):

        provider = self.provider("chat")

        prompt = self.build_prompt(message)

        return provider.ask(prompt)

    def ask_image(self, prompt):

        provider = self.provider("image")

        return provider.generate_image(prompt)

    def ask_video(self, prompt):

        provider = self.provider("video")

        return provider.generate_video(prompt)

    def ask_audio(self, prompt):

        provider = self.provider("audio")

        return provider.ask(prompt)