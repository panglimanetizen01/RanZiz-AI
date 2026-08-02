"""
RanZiz AI Brain Router
Version 1.0
"""


class BrainRouter:


    def __init__(

        self,

        commands,

        plugins,

        router,

        runtime

    ):

        self.commands = commands

        self.plugins = plugins

        self.router = router

        self.runtime = runtime


    def execute(

        self,

        message,

        context

    ):

        command = self.commands.execute(

            message

        )

        if command is not None:

            return command


        for plugin in self.plugins.plugins.values():

            result = plugin.chat(

                message

            )

            if result is not None:

                return result


        result = self.router.execute(

            message,

            context

        )

        if result is not None:

            return result


        return self.runtime.execute(

            message,

            context

        )