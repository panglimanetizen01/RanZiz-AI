"""
RanZiz AI Info Plugin
Version 2.0
"""

from src.config.config import Config


class Plugin:

    name = "Info"

    version = "2.0"

    author = Config.DEVELOPER

    description = "Plugin informasi RanZiz AI."

    def chat(self, message, context=None):

        text = message.strip().lower()

        if text == "developer":
            return f"Developer RanZiz AI : {Config.DEVELOPER}"

        if text == "project":
            return f"Project : {Config.APP_NAME}"

        if text == "version":
            return f"Version : {Config.VERSION}"

        return None

    def info(self):
        return {
            "name": self.name,
            "version": self.version,
            "author": self.author,
            "description": self.description,
        }
