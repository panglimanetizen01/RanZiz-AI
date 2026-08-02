from typing import ClassVar

"""
RanZiz AI Pop Library
Version 1.0
"""


class PopLibrary:

    NAME = "POP"

    STYLE: ClassVar = {

        "bpm": "72-95",

        "vocal": "Expressive",

        "language": "Simple",

        "structure": [

            "Verse 1",

            "Pre Chorus",

            "Chorus",

            "Verse 2",

            "Bridge",

            "Final Chorus"

        ],

        "instruments": [

            "Piano",

            "Acoustic Guitar",

            "Strings",

            "Bass",

            "Drums"

        ]

    }

    def get(self):

        return self.STYLE