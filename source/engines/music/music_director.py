"""
RanZiz AI Music Director
Version 1.0
"""


class MusicDirector:

    def direct(self, request):

        topic = (request.get("topic") or "").upper()

        emotion = (request.get("emotion") or "").upper()

        genre = request.get("genre")

        if genre:

            genre = genre.upper()

        else:

            genre = self.choose_genre(topic, emotion)

        return {

            "genre": genre,

            "bpm": self.choose_bpm(genre, emotion),

            "vocal": self.choose_vocal(topic, emotion),

            "duration": "03:30",

            "language": request.get(
                "language",
                "Indonesia"
            )

        }

    def choose_genre(self, topic, emotion):

        if emotion == "SAD":

            return "POP"

        if emotion == "HAPPY":

            return "POP"

        if topic == "PATAH HATI":

            return "POP"

        return "POP"

    def choose_bpm(self, genre, emotion):

        if emotion == "SAD":

            return 72

        if emotion == "HAPPY":

            return 94

        return 84

    def choose_vocal(self, topic, emotion):

        if emotion == "SAD":

            return "Female Emotional"

        return "Male Pop"