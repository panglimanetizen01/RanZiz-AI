from typing import ClassVar

"""
RanZiz AI Concept Engine
Version 1.0
"""


class ConceptEngine:

    CONCEPTS: ClassVar = {

        "kasih sayang": [
            "pelukan",
            "kehangatan",
            "perhatian",
            "ketulusan"
        ],

        "pengorbanan": [
            "air mata",
            "perjuangan",
            "pengabdian",
            "kesabaran"
        ],

        "doa": [
            "harapan",
            "langit",
            "keikhlasan",
            "kepercayaan"
        ],

        "keluarga": [
            "rumah",
            "kebersamaan",
            "kenangan",
            "cinta"
        ],

        "cinta": [
            "rindu",
            "setia",
            "hati",
            "kasih"
        ]

    }

    def expand(self, keywords):

        results = []

        for keyword in keywords:

            results.append(keyword)

            for item in self.CONCEPTS.get(keyword, []):

                if item not in results:

                    results.append(item)

        return results