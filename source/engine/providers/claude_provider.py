from typing import ClassVar

"""
RanZiz AI Claude Provider
Version 1.0
"""

from source.engine.providers.base_provider import BaseProvider


class ClaudeProvider(BaseProvider):

    name = "claude"

    capabilities: ClassVar = {
        "chat": True,
        "image": False,
        "video": False,
        "audio": False,
    }

    def ask(self, prompt):

        return (
            "[Claude Provider]\n"
            "API belum dikonfigurasi."
        )

    def chat(self, messages):

        return self.ask(messages)

    def generate_image(self, prompt):

        return (
            "[Claude Provider]\n"
            "Generate image tidak didukung."
        )

    def generate_video(self, prompt):

        return (
            "[Claude Provider]\n"
            "Generate video tidak didukung."
        )

    def models(self):

        return [
            "claude-opus-4.1",
            "claude-sonnet-4",
        ]


Provider = ClaudeProvider