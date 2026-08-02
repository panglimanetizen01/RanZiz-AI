"""
RanZiz AI Plugin Service
Version 1.1
"""

from source.events.event_bus import EventBus
from source.plugins.plugin_manager import PluginManager


class PluginService:

    def __init__(self):

        self.manager = PluginManager()

        self.bus = EventBus()

    def handle(self, message):

        for plugin in self.manager.plugins.values():

            result = plugin.chat(message)

            if result is not None:

                self.bus.publish(
                    "plugin.executed",
                    {
                        "plugin": plugin.name,
                        "message": message,
                        "result": result,
                    }
                )

                return result

        return None

    def subscribe(self, event, callback):

        self.bus.subscribe(
            event,
            callback
        )

    def list_plugins(self):

        return self.manager.list_plugins()

    def active_plugin(self):

        return self.manager.get_active_plugin()

    def set_active_plugin(self, name):

        return self.manager.set_active_plugin(name)