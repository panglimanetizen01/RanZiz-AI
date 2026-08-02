from typing import ClassVar

"""
RanZiz AI Genre Analyzer
Version 1.0
"""


class GenreAnalyzer:

    GENRES: ClassVar = {

        "pop": "POP",

        "dangdut": "DANGDUT",

        "koplo": "DANGDUT",

        "rock": "ROCK",

        "metal": "METAL",

        "hiphop": "HIPHOP",

        "hip hop": "HIPHOP",

        "rap": "HIPHOP",

        "edm": "EDM",

        "jazz": "JAZZ",

        "reggae": "REGGAE",

        "country": "COUNTRY",

        "keroncong": "KERONCONG",

        "nasyid": "NASYID"

    }

    def analyze(self, text):

        text = text.lower()

        for keyword, genre in self.GENRES.items():

            if keyword in text:

                return genre

        return "POP"