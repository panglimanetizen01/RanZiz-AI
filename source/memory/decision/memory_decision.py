"""
RanZiz AI Memory Decision Engine
Version 1.0
"""


class MemoryDecision:


    def decide(

        self,

        message

    ):

        text = message.lower()


        if any(word in text for word in [

            "siapa saya",

            "nama saya",

            "profil saya",

            "tentang saya"

        ]):

            return {

                "action": "memory",

                "confidence": 0.98

            }



        if any(word in text for word in [

            "kemarin",

            "terakhir",

            "lanjutkan",

            "sebelumnya"

        ]):

            return {

                "action": "episode",

                "confidence": 0.90

            }



        if any(word in text for word in [

            "buatkan",

            "jelaskan",

            "analisis",

            "rancang"

        ]):

            return {

                "action": "ai_engine",

                "confidence": 0.95

            }



        return {

            "action": "unknown",

            "confidence": 0.0

        }



    def __repr__(self):

        return "MemoryDecision()"