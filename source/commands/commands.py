"""
RanZiz AI Commands
Version 2.0
"""

from datetime import UTC, datetime

from source.commands.capability_command import CapabilityCommand


class Commands:


    def __init__(self):

        self.capability = CapabilityCommand()


    def execute(self, text):

        text = text.lower().strip()


        capability_result = self.capability.execute(
            text
        )

        if capability_result is not None:

            return capability_result


        if text in [
            "halo",
            "hai",
            "hi"
        ]:

            return "Halo! Senang bertemu denganmu."


        if text == "siapa kamu":

            return "Aku RanZiz AI yang sedang dikembangkan."


        if text == "versi":

            return "RanZiz AI v1.0"


        if text == "jam":

            return datetime.now(UTC).strftime(
                "Sekarang pukul %H:%M:%S"
            )


        if text == "tanggal":

            return datetime.now(UTC).strftime(
                "Hari ini %d-%m-%Y"
            )


        return None
