"""
RanZiz AI Episode Manager
Version 1.1
"""

from source.memory.episode.episodic_memory import EpisodicMemory


class EpisodeManager:


    def __init__(self):

        self.memory = EpisodicMemory()



    def remember(
        self,
        event,
        category="conversation"
    ):

        return self.memory.record(
            event,
            category
        )



    def all(self):

        return self.memory.all()



    def recent(
        self,
        limit=5
    ):

        return self.memory.latest(
            limit
        )



    def find(
        self,
        keyword
    ):

        return self.memory.search(
            keyword
        )



    def summary(self):

        episodes = self.memory.latest(
            5
        )

        if not episodes:

            return "Belum ada riwayat."


        result = []


        for item in episodes:

            result.append(
                f"{item['timestamp']} - {item['event']}"
            )


        return "\n".join(
            result
        )



    def __repr__(self):

        return "EpisodeManager()"