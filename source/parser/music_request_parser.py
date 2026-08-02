from typing import ClassVar

"""
RanZiz AI Music Request Parser
Version 2.1
"""


class MusicRequestParser:


    GENRES: ClassVar = {

        "POP": [
            "pop"
        ],

        "DANGDUT": [
            "dangdut",
            "koplo"
        ],

        "ROCK": [
            "rock"
        ],

        "HIPHOP": [
            "hiphop",
            "hip hop",
            "rap"
        ]

    }


    EMOTIONS: ClassVar = {

        "SAD": [
            "sedih",
            "galau",
            "nangis",
            "haru",
            "kehilangan"
        ],

        "HAPPY": [
            "bahagia",
            "senang",
            "ceria"
        ],

        "SPIRIT": [
            "semangat",
            "motivasi",
            "perjuangan",
            "pantang menyerah"
        ]

    }


    TOPICS: ClassVar = {

        "IBU": [
            "ibu",
            "emak",
            "mama",
            "bunda"
        ],

        "AYAH": [
            "ayah",
            "bapak",
            "papa"
        ],

        "CINTA": [
            "cinta",
            "pacar",
            "sayang"
        ],

        "PERJUANGAN": [
            "perjuangan",
            "mimpi",
            "sukses",
            "bangkit"
        ],

        "KEHIDUPAN": [
            "kehidupan",
            "hidup",
            "nasib"
        ]

    }


    def parse(self, text):

        text = text.lower()

        return {

            "genre": self.find(text, self.GENRES),

            "emotion": self.find(text, self.EMOTIONS),

            "topic": self.find(text, self.TOPICS),

            "language": "Indonesia",

            "output": "MP3"

        }


    def find(self, text, data):

        for value, words in data.items():

            for word in words:

                if word in text:

                    return value

        return None