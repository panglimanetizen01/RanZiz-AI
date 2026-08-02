"""
RanZiz AI Command Handler
Version 1.0
"""


class CommandHandler:

    def __init__(
        self,
        commands
    ):
        self.commands = commands


    def handle(
        self,
        message,
        session,
        context,
        response_builder
    ):

        command = self.commands.execute(
            message
        )

        if command is None:
            return None

        session.add_message(
            "assistant",
            command
        )

        return response_builder(
            session,
            context,
            command
        )
