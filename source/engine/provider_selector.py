from typing import ClassVar

"""
RanZiz AI Provider Selector
Version 2.0
"""

from source.engine.provider_manager import ProviderManager


class ProviderSelector:

    PRIORITY: ClassVar = {
        "chat": [
            "local",
            "gemini",
            "openai",
            "claude",
            "deepseek",
            "ollama",
        ],
        "image": [
            "gemini",
            "openai",
        ],
        "video": [
            "local",
        ],
        "audio": [
            "gemini",
            "openai",
            "local",
        ],
    }

    def __init__(self):

        self.manager = ProviderManager()

    def select(self, capability="chat"):

        priority = self.PRIORITY.get(capability, [])

        for name in priority:

            provider = self.manager.get(name)

            if provider and provider.supports(capability):

                return provider

        provider = self.manager.get_by_capability(capability)

        if provider:

            return provider

        return self.manager.get("local")

    def select_chat(self):

        return self.select("chat")

    def select_image(self):

        return self.select("image")

    def select_video(self):

        return self.select("video")

    def select_audio(self):

        return self.select("audio")