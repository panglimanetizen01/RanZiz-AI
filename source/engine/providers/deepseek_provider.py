from typing import ClassVar

"""
RanZiz AI DeepSeek Provider
Version 1.0
"""

from source.engine.providers.base_provider import BaseProvider


class DeepSeekProvider(BaseProvider):

    name = "deepseek"

    capabilities: ClassVar = {
        "chat": True,
        "image": False,
        "video": False,
        "audio": False,
    }

    def ask(self, prompt):

        return (
            "[DeepSeek Provider]\n"
            "API belum dikonfigurasi."
        )

    def chat(self, messages):

        return self.ask(messages)

    def generate_image(self, prompt):

        return (
            "[DeepSeek Provider]\n"
            "Generate image tidak didukung."
        )

    def generate_video(self, prompt):

        return (
            "[DeepSeek Provider]\n"
            "Generate video tidak didukung."
        )

    def models(self):

        return [
            "deepseek-chat",
            "deepseek-reasoner",
        ]


Provider = DeepSeekProvider