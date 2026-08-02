"""
RanZiz AI Smart Memory Extractor
Version 1.0
"""

import re


class SmartMemoryExtractor:


    def extract(

        self,

        message

    ):

        text = message.strip()


        patterns = [

            (
                r"(?i)^nama saya (.+)$",
                "nama"
            ),

            (
                r"(?i)^aku bernama (.+)$",
                "nama"
            ),

            (
                r"(?i)^saya suka (.+)$",
                "suka"
            ),

            (
                r"(?i)^warna favorit saya (.+)$",
                "warna_favorit"
            ),

            (
                r"(?i)^genre favorit saya (.+)$",
                "genre_favorit"
            ),

            (
                r"(?i)^hobi saya (.+)$",
                "hobi"
            )

        ]


        for pattern, key in patterns:

            match = re.match(

                pattern,

                text

            )

            if match:

                return {

                    "saved": True,

                    "key": key,

                    "value": match.group(1).strip()

                }


        return {

            "saved": False

        }


    def __repr__(self):

        return "SmartMemoryExtractor()"