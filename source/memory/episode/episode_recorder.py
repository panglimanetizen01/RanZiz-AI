"""
RanZiz AI Episode Recorder
Version 1.1
"""

from source.memory.episode.episode_filter import EpisodeFilter


class EpisodeRecorder:


    def __init__(self):

        self.filter = EpisodeFilter()



    def record(
        self,
        gateway,
        message,
        metadata=None
    ):

        if not self.filter.should_record(
            message
        ):

            return None


        category = self.filter.category(
            message
        )


        event = message


        if metadata is not None:

            event = {
                "message": message,
                "metadata": metadata
            }


        return gateway.remember(
            event,
            category
        )



    def __repr__(self):

        return "EpisodeRecorder()"