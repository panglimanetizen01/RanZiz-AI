"""
RanZiz AI Decision Engine
Version 1.0
"""


class DecisionEngine:

    def decide(self, request):

        plan = {
            "engines": [],
            "outputs": []
        }

        goal = request.get("goal")

        if goal == "MUSIC":

            plan["engines"] = [
                "MusicEngine",
                "ImageEngine",
                "VideoEngine"
            ]

            plan["outputs"] = [
                "lyrics.txt",
                "cover.png",
                "song.mp3",
                "lyric_video.mp4"
            ]

        elif goal == "VIDEO":

            plan["engines"] = [
                "ImageEngine",
                "VoiceEngine",
                "VideoEngine"
            ]

            plan["outputs"] = [
                "video.mp4"
            ]

        elif goal == "IMAGE":

            plan["engines"] = [
                "ImageEngine"
            ]

            plan["outputs"] = [
                "image.png"
            ]

        elif goal == "WEBSITE":

            plan["engines"] = [
                "CodeEngine"
            ]

            plan["outputs"] = [
                "website.zip"
            ]

        elif goal == "APPLICATION":

            plan["engines"] = [
                "CodeEngine"
            ]

            plan["outputs"] = [
                "application.zip"
            ]

        return plan