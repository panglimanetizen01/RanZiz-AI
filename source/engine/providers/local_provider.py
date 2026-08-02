from typing import ClassVar

"""
RanZiz AI Local Provider
Version 3.0
"""

from source.engine.providers.base_provider import BaseProvider


class LocalProvider(BaseProvider):

    name = "local"

    capabilities: ClassVar = {
        "chat": True,
        "image": False,
        "video": False,
        "audio": False,
    }

    def ask(self, prompt):

        text = str(prompt).lower()

        if "=== user ===" in text:
            text = text.split("=== user ===")[-1].strip()

        if text in ("halo", "hai", "hi"):
            return "Halo! Senang bertemu denganmu."

        if text == "apa kabar":
            return "Baik. Ada yang bisa saya bantu?"

        if "python" in text:
            return (
                "Python adalah bahasa pemrograman tingkat tinggi yang "
                "banyak digunakan untuk AI, web, otomasi, data science, "
                "dan berbagai aplikasi lainnya."
            )

        if "terima kasih" in text or "makasih" in text:
            return "Sama-sama. Senang bisa membantu."

        return (
            "Saya memahami pesan Anda, tetapi Local Provider masih "
            "merupakan AI offline sederhana. Hubungkan RanZiz AI ke "
            "provider seperti Ollama, OpenAI, atau Groq untuk mendapatkan "
            "jawaban yang lebih cerdas."
        )

    def chat(self, messages):

        return self.ask(str(messages))

    def generate_image(self, prompt):

        return "Local Provider belum mendukung generate image."

    def generate_video(self, prompt):

        return "Local Provider belum mendukung generate video."

    def models(self):

        return [
            "local"
        ]


Provider = LocalProvider