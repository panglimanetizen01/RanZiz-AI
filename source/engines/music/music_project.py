"""
RanZiz AI Music Project
Version 2.0
"""

from source.engines.music.music_blueprint import MusicBlueprint


class MusicProject:

    def __init__(self):

        self.blueprint = MusicBlueprint()

    def build(

        self,

        metadata,

        story,

        structure,

        rhyme,

        lyrics

    ):

        return self.blueprint.build(

            metadata,

            story,

            structure,

            rhyme,

            lyrics

        )