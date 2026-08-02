from typing import ClassVar

"""
RanZiz AI OpenAI Provider
Version 1.0
"""

from source.engine.providers.base_provider import BaseProvider


class OpenAIProvider(BaseProvider):

    name = "openai"

    capabilities: ClassVar = {
        "chat": True,
        "image": True,
        "video": False,
        "audio": True,
    }

    def ask(self, prompt):

        return (
            "[OpenAI Provider]\n"
            "API belum dikonfigurasi."
        )

    def chat(self, messages):

        return self.ask(messages)

    def generate_image(self, prompt):

        return (
            "[OpenAI Provider]\n"
            "Generate image belum diaktifkan."
        )

    def generate_video(self, prompt):

        return (
            "[OpenAI Provider]\n"
            "Generate video belum didukung."
        )

    def models(self):

        return [
            "gpt-5.5",
            "gpt-5.5-mini",
            "gpt-image-1",
        ]


Provider = OpenAIProvider