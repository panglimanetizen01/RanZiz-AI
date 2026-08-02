from typing import ClassVar

"""
RanZiz AI Gemini Provider
Version 1.0
"""

from source.engine.providers.base_provider import BaseProvider


class GeminiProvider(BaseProvider):

    name = "gemini"

    capabilities: ClassVar = {
        "chat": True,
        "image": True,
        "video": False,
        "audio": True,
    }

    def ask(self, prompt):

        return (
            "[Gemini Provider]\n"
            "API belum dikonfigurasi."
        )

    def chat(self, messages):

        return self.ask(messages)

    def generate_image(self, prompt):

        return (
            "[Gemini Provider]\n"
            "Generate image belum diaktifkan."
        )

    def generate_video(self, prompt):

        return (
            "[Gemini Provider]\n"
            "Generate video belum didukung."
        )

    def models(self):

        return [
            "gemini-2.5-pro",
            "gemini-2.5-flash",
        ]


Provider = GeminiProvider