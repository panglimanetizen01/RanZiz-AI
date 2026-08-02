"""
RanZiz AI Music Blueprint
Version 1.0
"""


class MusicBlueprint:

    def build(
        self,
        metadata,
        story,
        structure,
        rhyme,
        lyrics
    ):

        return {

            "metadata": metadata,

            "story": story,

            "structure": structure,

            "rhyme": rhyme,

            "lyrics": lyrics,

            "render": {

                "audio": True,

                "cover": True,

                "lyric_video": True,

                "music_video": True

            }

        }