"""
RanZiz AI Integration Test
Version 1.0
"""

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from source.core.brain import Brain


class IntegrationTest(unittest.TestCase):

    def setUp(self):

        self.brain = Brain()

    def test_chat_flow(self):

        result = self.brain.process(
            "Halo"
        )

        self.assertIsNotNone(result)

    def test_music_flow(self):

        result = self.brain.process(
            "buat lagu dangdut tentang perjuangan"
        )

        self.assertIsNotNone(result)

    def test_project_flow(self):

        result = self.brain.process(
            "status project"
        )

        self.assertIsNotNone(result)

    def test_coding_flow(self):

        result = self.brain.process(
            "debug python"
        )

        self.assertIsNotNone(result)

    def test_empty_flow(self):

        result = self.brain.process(
            ""
        )

        self.assertIsNotNone(result)


if __name__ == "__main__":

    unittest.main(
        verbosity=2
    )