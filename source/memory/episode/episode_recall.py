"""
RanZiz AI Episode Recall
Version 1.0
"""

from source.memory.episode.episode_manager import EpisodeManager


class EpisodeRecall:


    def __init__(self):

        self.manager = EpisodeManager()



    def latest(

        self,

        limit=1

    ):

        episodes = self.manager.recent(

            limit

        )

        if not episodes:

            return "Belum ada riwayat."



        result = []

        for item in episodes:

            result.append(

                item.get(

                    "event",

                    ""

                )

            )


        return "\n".join(

            result

        )



    def search(

        self,

        keyword

    ):

        episodes = self.manager.find(

            keyword

        )


        if not episodes:

            return "Tidak ada riwayat ditemukan."



        result = []

        for item in episodes:

            result.append(

                item.get(

                    "event",

                    ""

                )

            )


        return "\n".join(

            result

        )



    def recall(

        self,

        message

    ):

        text = message.lower()


        if (

            "terakhir" in text

            or "baru saja" in text

            or "kemarin" in text

        ):

            return self.latest()



        if "project" in text:

            return self.search(

                "ranziz"

            )


        return None



    def __repr__(self):

        return "EpisodeRecall()"