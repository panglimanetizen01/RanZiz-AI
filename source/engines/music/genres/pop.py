from typing import ClassVar

from .base_genre import BaseGenre


class PopGenre(BaseGenre):

    NAME = "POP"

    BPM = 90

    STYLE = "Modern Pop"

    INSTRUMENTS: ClassVar = [
        "Piano",
        "Guitar",
        "Bass",
        "Drums"
    ]

    VOCAL = "Clean"