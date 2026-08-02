from typing import ClassVar

"""
RanZiz AI Line Generator
Version 1.0
"""


class LineGenerator:

    DATABASE: ClassVar = {

        "IBU": {

            "SAD": [

                "Langkahmu selalu mengiringi hidupku,",
                "Doamu menjadi cahaya di setiap jalanku,",
                "Tak pernah lelah kau menjaga hatiku,",
                "Kasihmu akan selalu hidup dalam jiwaku,"

            ],

            "HAPPY": [

                "Senyummu menghangatkan hariku,",
                "Pelukmu selalu menjadi rumahku,",
                "Bahagiamu adalah bahagiaku,",
                "Terima kasih untuk semua cintamu,"

            ]

        }

    }

    def generate(self, topic, emotion):

        topic = (topic or "IBU").upper()

        emotion = (emotion or "HAPPY").upper()

        topic_data = self.DATABASE.get(topic)

        if topic_data is None:

            return [

                "Kisah ini dimulai dari sebuah harapan,",
                "Langkah terus berjalan menuju masa depan,",
                "Setiap perjalanan menyimpan kenangan,",
                "Semoga semua berakhir dengan kebahagiaan,"

            ]

        return topic_data.get(
            emotion,
            topic_data["HAPPY"]
        )