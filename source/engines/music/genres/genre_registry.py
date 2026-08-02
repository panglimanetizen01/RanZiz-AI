from .dangdut import DangdutGenre
from .pop import PopGenre


class GenreRegistry:

    def __init__(self):

        self.genres = {

            "POP": PopGenre(),

            "DANGDUT": DangdutGenre()

        }

    def get(self, name):

        if not name:
            return self.genres["POP"]

        return self.genres.get(
            name.upper(),
            self.genres["POP"]
        )