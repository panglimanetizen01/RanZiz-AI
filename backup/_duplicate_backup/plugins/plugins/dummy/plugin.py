"""
RanZiz AI Dummy Plugin

Plugin ini digunakan untuk menguji
apakah Plugin Loader dapat menemukan
dan memuat plugin dengan benar.
"""


class Plugin:

    name = "Dummy"

    version = "2.0"

    author = "RanZiz AI"

    description = "Plugin dummy untuk pengujian."

    def chat(self, message, context=None):

        text = message.strip().lower()

        keywords = (
            "dummy",
            "tes plugin",
            "test plugin",
            "plugin dummy"
        )

        if text not in keywords:

            return None

        return (
            "[Dummy Plugin] "
            "Plugin berhasil berjalan."
        )

    def info(self):

        return {
            "name": self.name,
            "version": self.version,
            "author": self.author,
            "description": self.description,
        }