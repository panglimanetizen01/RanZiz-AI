from typing import ClassVar

"""
RanZiz AI Base Provider
Version 2.1
"""


class BaseProvider:

    name = "base"

    capabilities: ClassVar = {
        "chat": False,
        "image": False,
        "video": False,
        "audio": False,
    }

    def ask(self, prompt):
        raise NotImplementedError

    def chat(self, messages):
        raise NotImplementedError

    def generate_image(self, prompt):
        raise NotImplementedError

    def generate_video(self, prompt):
        raise NotImplementedError

    def models(self):
        return []

    def supports(self, feature):
        return self.capabilities.get(feature, False)

    def info(self):
        return {
            "name": self.name,
            "models": self.models(),
            "capabilities": self.capabilities,
        }