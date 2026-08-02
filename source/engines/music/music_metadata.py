"""
RanZiz AI Music Metadata
Version 2.0
"""

from source.engines.music.library import LibraryManager


class MusicMetadata:

    def __init__(self):

        self.library = LibraryManager()

    def create(self, request):

        genre = (request.get("genre") or "POP").upper()

        style = self.library.get(genre)

        return {

            "genre": genre,

            "language": request.get(
                "language",
                "Indonesia"
            ),

            "emotion": request.get(
                "emotion",
                "HAPPY"
            ),

            "topic": request.get(
                "topic",
                "KEHIDUPAN"
            ),

            "output": request.get(
                "output",
                "MP3"
            ),

            "bpm": style["bpm"],

            "vocal": style["vocal"],

            "instruments": style["instruments"],

            "structure": style["structure"]

        }