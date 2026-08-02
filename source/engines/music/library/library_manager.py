"""
RanZiz AI Library Manager
Version 1.0
"""

from source.engines.music.library.pop_library import PopLibrary


class LibraryManager:

    def __init__(self):

        self.libraries = {

            "POP": PopLibrary()

        }

    def get(self, genre):

        genre = (genre or "POP").upper()

        if genre not in self.libraries:

            genre = "POP"

        return self.libraries[genre].get()