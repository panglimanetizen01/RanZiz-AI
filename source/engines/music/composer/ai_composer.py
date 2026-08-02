"""
RanZiz AI Composer
Version 4.0
"""

from source.engines.music.composer.line_generator import LineGenerator


class AIComposer:

    def __init__(self):

        self.line_generator = LineGenerator()

    def compose(self, story, structure, rhyme):

        lyrics = []

        lyrics.append(f"Judul : {story['title']}")
        lyrics.append(f"Rima : {rhyme}")
        lyrics.append("")

        lines = self.line_generator.generate(
            story["topic"],
            story["emotion"]
        )

        for section in structure:

            lyrics.append(f"[{section}]")

            if section == "Verse 1":

                lyrics.extend(lines[:2])

            elif section == "Pre Chorus":

                lyrics.append(story["conflict"])

            elif section == "Chorus":

                lyrics.extend(lines)

            elif section == "Verse 2":

                lyrics.extend(lines[2:])

            elif section == "Bridge":

                lyrics.append(story["climax"])

            elif section == "Final Chorus":

                lyrics.extend(lines)

            lyrics.append("")

        return "\n".join(lyrics)