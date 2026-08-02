"""
RanZiz AI Session Integration Test
Version 1.0
"""

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from source.core.brain import Brain


class SessionIntegrationTest(unittest.TestCase):

    def setUp(self):

        self.brain = Brain()

    def test_same_session(self):

        session = "integration-session"

        self.brain.process(
            "Halo",
            session
        )

        result = self.brain.process(
            "status project",
            session
        )

        self.assertIsNotNone(
            result
        )

    def test_different_sessions(self):

        result1 = self.brain.process(
            "Halo",
            "session-1"
        )

        result2 = self.brain.process(
            "Halo",
            "session-2"
        )

        self.assertIsNotNone(result1)
        self.assertIsNotNone(result2)

    def test_music_then_chat(self):

        session = "music-chat"

        self.brain.process(
            "buat lagu pop",
            session
        )

        result = self.brain.process(
            "Halo",
            session
        )

        self.assertIsNotNone(
            result
        )


if __name__ == "__main__":

    unittest.main(
        verbosity=2
    )