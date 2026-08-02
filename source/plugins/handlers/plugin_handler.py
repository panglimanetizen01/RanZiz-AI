"""
RanZiz AI Plugin Handler
Version 1.0
"""


class PluginHandler:

    def __init__(
        self,
        plugin_manager
    ):
        self.plugin_manager = plugin_manager


    def handle(
        self,
        message,
        session,
        context,
        response_builder
    ):

        plugins = getattr(
            self.plugin_manager,
            "plugins",
            {}
        )

        for plugin in plugins.values():

            result = plugin.chat(
                message
            )

            if result is not None:

                session.add_message(
                    "assistant",
                    result
                )

                return response_builder(
                    session,
                    context,
                    result
                )

        return None
