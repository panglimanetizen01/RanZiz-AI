"""
RanZiz AI Auto Memory Engine
Version 1.1
"""

from source.memory.engine.smart_memory_extractor import SmartMemoryExtractor
from source.memory.memory_service import MemoryService


class AutoMemoryEngine:


    def __init__(self):

        self.memory = MemoryService()

        self.extractor = SmartMemoryExtractor()


    def process(

        self,

        message

    ):

        text = message.strip()

        lower = text.lower()


        if "=" in text:

            key, value = text.split("=", 1)

            key = key.strip()

            value = value.strip()

            self.memory.remember(

                key,

                value

            )

            return {

                "saved": True,

                "key": key,

                "value": value

            }


        if lower.startswith("ingat "):

            content = text[6:].strip()

            if ":" in content:

                key, value = content.split(":", 1)

                key = key.strip()

                value = value.strip()

                self.memory.remember(

                    key,

                    value

                )

                return {

                    "saved": True,

                    "key": key,

                    "value": value

                }


        smart = self.extractor.extract(

            text

        )

        if smart["saved"]:

            self.memory.remember(

                smart["key"],

                smart["value"]

            )

            return smart


        return {

            "saved": False

        }


    def __repr__(self):

        return "AutoMemoryEngine()"