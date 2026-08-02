"""
RanZiz AI Music Engine
Version 2.0
"""

from source.engines.base_engine import BaseEngine
from source.engines.music.lyric_generator import LyricGenerator
from source.engines.music.music_metadata import MusicMetadata
from source.engines.music.music_project import MusicProject


class MusicEngine(BaseEngine):

    NAME = "MusicEngine"

    def __init__(self):

        self.metadata = MusicMetadata()
        self.lyrics = LyricGenerator()
        self.project = MusicProject()

    def run(self, project, request):

        metadata = self.metadata.create(request)

        story = self.lyrics.story_builder.build(
            request
        )

        structure = self.lyrics.structure_builder.build()

        rhyme = self.lyrics.rhyme_builder.build(
            request.get("emotion")
        )

        lyrics = self.lyrics.composer.compose(
            story,
            structure,
            rhyme
        )

        return self.project.build(
            metadata,
            story,
            structure,
            rhyme,
            lyrics
        )