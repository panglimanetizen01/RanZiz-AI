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

            if hasattr(metadata, "to_dict"):
                metadata = metadata.to_dict()

            elif not isinstance(
                metadata,
                (str, int, float, bool, list, dict, type(None))
            ):
                metadata = str(metadata)

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