"""
RanZiz AI Regression Test
Version 1.0
"""

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from source.core.brain import Brain


class RegressionTest(unittest.TestCase):

    def setUp(self):

        self.brain = Brain()

    def test_core_commands(self):

        commands = [

            "Halo",

            "status project",

            "debug python",

            "buat lagu pop",

            "buat lagu dangdut tentang perjuangan",

            ""

        ]

        for command in commands:

            result = self.brain.process(command)

            self.assertIsNotNone(result)


if __name__ == "__main__":

    unittest.main(
        verbosity=2
    )