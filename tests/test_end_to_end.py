"""
RanZiz AI End-to-End Test
Version 1.0
"""

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from source.core.brain import Brain


class EndToEndTest(unittest.TestCase):

    def setUp(self):

        self.brain = Brain()
        self.session = "e2e-test"

    def test_complete_conversation(self):

        messages = [

            "Halo",

            "status project",

            "debug python",

            "buat lagu dangdut tentang perjuangan",

            "apa itu python"

        ]

        for message in messages:

            result = self.brain.process(

                message,

                self.session

            )

            self.assertIsNotNone(result)

    def test_empty_then_chat(self):

        self.assertIsNotNone(

            self.brain.process(

                "",

                self.session

            )

        )

        self.assertIsNotNone(

            self.brain.process(

                "Halo",

                self.session

            )

        )


if __name__ == "__main__":

    unittest.main(

        verbosity=2

    )