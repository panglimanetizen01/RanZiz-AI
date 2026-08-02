"""
RanZiz AI Memory Classifier
Version 1.0
"""


class MemoryClassifier:


    def classify(

        self,

        key,

        value

    ):

        key = key.lower()


        identity = {

            "nama",

            "username",

            "umur",

            "usia",

            "kota"

        }


        preference = {

            "warna_favorit",

            "genre_favorit",

            "favorite_genre",

            "hobi",

            "suka"

        }


        project = {

            "project",

            "aplikasi",

            "ai",

            "ranziz"

        }


        if key in identity:

            return "identity"


        if key in preference:

            return "preference"


        if key in project:

            return "project"


        return "general"


    def __repr__(self):

        return "MemoryClassifier()"