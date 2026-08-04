"""
RanZiz AI Composer Executor
Version 3.0
"""

from source.capability.base_executor import BaseCapabilityExecutor
from source.capability.schema.capability_info import CapabilityInfo


class ComposerExecutor(BaseCapabilityExecutor):


    def execute(self, payload):

        context = payload.get("context")


        lyrics = ""

        if context:

            lyrics = context.get(
                "Lyric Engine",
                ""
            )

        return self.success(
            {
                "source_lyrics_available": bool(lyrics),

                "composition": "READY"
            }
        )


    def metadata(self):

        return CapabilityInfo(

            name="Composer",

            category="Music",

            description="Menyusun struktur komposisi lagu",

            inputs=[
                "lyrics"
            ],

            outputs=[
                "composition"
            ],

            requires=[
                "Lyric Engine"
            ],

            priority=20

        )