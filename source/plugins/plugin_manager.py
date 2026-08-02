"""
RanZiz AI Plugin Manager
Version 2.0
"""

from source.plugins.plugin_loader import PluginLoader


class PluginManager:

    def __init__(self):

        self.loader = PluginLoader()
        self.plugins = self.loader.load_all()
        self.active_plugin = None

        if self.plugins:
            self.active_plugin = next(
                iter(self.plugins.values())
            )


    def list_plugins(self):
        return list(self.plugins.keys())


    def get_plugin(self, name):
        return self.plugins.get(name)


    def validate_plugin(self, plugin):

        if plugin is None:
            return False

        if not hasattr(plugin, "name"):
            return False

        return hasattr(plugin, "chat")


    def get_active_plugin(self):
        return self.active_plugin


    def set_active_plugin(self, name):

        plugin = self.get_plugin(name)

        if not self.validate_plugin(plugin):
            return False

        self.active_plugin = plugin
        return True


    def active_name(self):

        if not self.validate_plugin(self.active_plugin):
            return None

        return self.active_plugin.name


    def execute(self, message):

        plugin = self.active_plugin

        if not self.validate_plugin(plugin):
            return {
                "status": "FAILED",
                "error": "Plugin aktif tidak valid"
            }

        try:
            result = plugin.chat(message)

            return {
                "status": "SUCCESS",
                "result": result
            }

        except Exception as error:  # noqa: BLE001
            # Plugin execution is isolated so plugin failures do not crash the application.
            return {
                "status": "FAILED",
                "error": str(error)
            }
