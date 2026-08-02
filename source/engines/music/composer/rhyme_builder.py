"""
RanZiz AI Rhyme Builder
Version 1.0
"""


class RhymeBuilder:

    def build(self, emotion):

        emotion = (emotion or "").upper()

        if emotion == "SAD":
            return "AABB"

        if emotion == "HAPPY":
            return "ABAB"

        if emotion == "ROMANTIC":
            return "AAAA"

        return "FREE"