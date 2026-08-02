"""
RanZiz AI Semantic Analyzer
Version 1.0
"""


class SemanticAnalyzer:

    def analyze(self, text):

        text = text.lower()

        data = {

            "emotion": "NORMAL",

            "topic": "GENERAL",

            "target": "GENERAL"

        }

        # Emotion

        if "sedih" in text:

            data["emotion"] = "SAD"

        elif "bahagia" in text:

            data["emotion"] = "HAPPY"

        elif "romantis" in text:

            data["emotion"] = "ROMANTIC"

        elif "semangat" in text:

            data["emotion"] = "ENERGETIC"

        # Topic

        if "ibu" in text:

            data["topic"] = "IBU"

        elif "ayah" in text:

            data["topic"] = "AYAH"

        elif "cinta" in text:

            data["topic"] = "CINTA"

        elif "indonesia" in text:

            data["topic"] = "INDONESIA"

        # Target

        if "anak" in text:

            data["target"] = "ANAK"

        elif "remaja" in text:

            data["target"] = "REMAJA"

        elif "dewasa" in text:

            data["target"] = "DEWASA"

        return data