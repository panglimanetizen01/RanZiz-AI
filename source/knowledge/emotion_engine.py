from typing import ClassVar

"""
RanZiz AI Emotion Engine
Version 1.0
"""


class EmotionEngine:

    EMOTIONS: ClassVar = {

        "SAD": {

            "tone": "Sedih",

            "words": [
                "air mata",
                "rindu",
                "kehilangan",
                "sunyi",
                "kenangan",
                "doa"
            ]

        },

        "HAPPY": {

            "tone": "Bahagia",

            "words": [
                "senyum",
                "tawa",
                "bahagia",
                "ceria",
                "harapan",
                "syukur"
            ]

        },

        "ROMANTIC": {

            "tone": "Romantis",

            "words": [
                "cinta",
                "hati",
                "rindu",
                "pelukan",
                "kasih",
                "setia"
            ]

        },

        "SPIRIT": {

            "tone": "Semangat",

            "words": [
                "berjuang",
                "bangkit",
                "mimpi",
                "harapan",
                "masa depan",
                "pantang menyerah"
            ]

        }

    }

    def get(self, emotion):

        emotion = (emotion or "HAPPY").upper()

        return self.EMOTIONS.get(

            emotion,

            self.EMOTIONS["HAPPY"]

        )