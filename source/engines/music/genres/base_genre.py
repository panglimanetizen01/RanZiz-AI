from typing import ClassVar

"""
RanZiz AI Base Genre
Version 1.0
"""


class BaseGenre:

    NAME = "BASE"

    BPM = 80

    STYLE = "GENERAL"

    INSTRUMENTS: ClassVar = []

    VOCAL = "GENERAL"

    STRUCTURE: ClassVar = [
        "Verse 1",
        "Pre Chorus",
        "Chorus",
        "Verse 2",
        "Bridge",
        "Final Chorus"
    ]