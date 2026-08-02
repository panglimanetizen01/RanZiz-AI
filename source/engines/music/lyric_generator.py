"""
RanZiz AI Lyric Generator
Version 2.0
"""

from source.engines.music.composer import (
    AIComposer,
    RhymeBuilder,
    StoryBuilder,
    StructureBuilder,
)


class LyricGenerator:

    def __init__(self):

        self.story_builder = StoryBuilder()
        self.structure_builder = StructureBuilder()
        self.rhyme_builder = RhymeBuilder()
        self.composer = AIComposer()

    def generate(self, request):

        story = self.story_builder.build(request)

        structure = self.structure_builder.build()

        rhyme = self.rhyme_builder.build(
            request.get("emotion")
        )

        lyrics = self.composer.compose(
            story,
            structure,
            rhyme
        )

        return lyrics