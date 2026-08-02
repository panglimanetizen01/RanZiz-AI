from typing import ClassVar

"""
RanZiz AI Ollama Provider
Version 1.0
"""

from source.engine.providers.base_provider import BaseProvider


class OllamaProvider(BaseProvider):

    name = "ollama"

    capabilities: ClassVar = {
        "chat": True,
        "image": False,
        "video": False,
        "audio": False,
    }

    def ask(self, prompt):

        return (
            "[Ollama Provider]\n"
            "Server Ollama belum dikonfigurasi."
        )

    def chat(self, messages):

        return self.ask(messages)

    def generate_image(self, prompt):

        return (
            "[Ollama Provider]\n"
            "Generate image tidak didukung."
        )

    def generate_video(self, prompt):

        return (
            "[Ollama Provider]\n"
            "Generate video tidak didukung."
        )

    def models(self):

        return [
            "llama3.3",
            "qwen3",
            "mistral",
            "gemma3",
        ]


Provider = OllamaProvider