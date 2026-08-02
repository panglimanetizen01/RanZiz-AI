"""
RanZiz AI Brain Test
Version 1.0
"""

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from source.core.brain import Brain


class BrainTest(unittest.TestCase):

    def setUp(self):

        self.brain = Brain()

    def test_instance(self):

        self.assertIsNotNone(
            self.brain
        )

    def test_startup(self):

        result = self.brain.startup()

        self.assertIsInstance(
            result,
            str
        )

        self.assertIn(
            "RanZiz AI",
            result
        )

    def test_empty_message(self):

        result = self.brain.process(
            ""
        )

        self.assertIsNotNone(
            result
        )

    def test_chat_message(self):

        result = self.brain.process(
            "Halo"
        )

        self.assertIsNotNone(
            result
        )

    def test_music_message(self):

        result = self.brain.process(
            "buat lagu pop"
        )

        self.assertIsNotNone(
            result
        )

    def test_project_message(self):

        result = self.brain.process(
            "status project"
        )

        self.assertIsNotNone(
            result
        )


if __name__ == "__main__":

    unittest.main(
        verbosity=2
    )