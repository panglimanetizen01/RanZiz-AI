"""
RanZiz AI Voice Engine
Version 1.0
"""

from source.engines.base_engine import BaseEngine


class VoiceEngine(BaseEngine):

    NAME = "VoiceEngine"

    def run(self, project, request):

        return {
            "type": "voice",
            "text": request.get(
                "text",
                ""
            ),
            "voice": request.get(
                "voice",
                "default"
            ),
            "status": "READY"
        }
