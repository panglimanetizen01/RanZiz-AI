from typing import ClassVar

from .base_genre import BaseGenre


class DangdutGenre(BaseGenre):

    NAME = "DANGDUT"

    BPM = 82

    STYLE = "Dangdut Modern"

    INSTRUMENTS: ClassVar = [
        "Kendang",
        "Seruling",
        "Bass",
        "Keyboard"
    ]

    VOCAL = "Dangdut"