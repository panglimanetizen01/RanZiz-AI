from typing import ClassVar

"""
RanZiz AI Topic Engine
Version 1.0
"""


class TopicEngine:

    DATA: ClassVar = {

        "IBU": {

            "keywords": [
                "kasih sayang",
                "pengorbanan",
                "doa",
                "keluarga",
                "cinta"
            ]

        },

        "AYAH": {

            "keywords": [
                "kerja keras",
                "pengorbanan",
                "pelindung",
                "keluarga",
                "teladan"
            ]

        },

        "CINTA": {

            "keywords": [
                "rindu",
                "setia",
                "harapan",
                "bahagia",
                "perpisahan"
            ]

        }

    }

    def get(self, topic):

        topic = topic.upper()

        return self.DATA.get(

            topic,

            {

                "keywords": [

                    topic.lower()

                ]

            }

        )