"""
RanZiz AI Plugin Runtime Capability
Version 1.0
"""


class PluginRuntimeCapability:


    def __init__(

        self,

        plugin_manager=None

    ):

        self.plugin_manager = plugin_manager


    def bind(

        self,

        plugin_manager

    ):

        self.plugin_manager = plugin_manager

        return self


    def execute(

        self,

        message,

        context=None

    ):

        if self.plugin_manager is None:

            return None


        for plugin in self.plugin_manager.plugins.values():

            result = plugin.chat(

                message

            )

            if result is not None:

                return result


        return None