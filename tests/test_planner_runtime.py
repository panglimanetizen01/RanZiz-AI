"""
RanZiz AI Planner Runtime Test
Version 1.0
"""

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from source.planner.planner_runtime import PlannerRuntime
from source.capability.result.capability_result import CapabilityResult


class DummyCapabilityExecutor:

    def execute(self, task):

        return CapabilityResult(

            task.capability,

            output=f"OK: {task.capability}"

        )


class PlannerRuntimeTest(unittest.TestCase):

    def setUp(self):

        self.runtime = PlannerRuntime(

            DummyCapabilityExecutor()

        )

    def test_music_runtime(self):

        result = self.runtime.execute(

            "buat lagu pop"

        )

        self.assertTrue(

            len(result) > 0

        )

    def test_coding_runtime(self):

        result = self.runtime.execute(

            "debug python"

        )

        self.assertTrue(

            len(result) > 0

        )


if __name__ == "__main__":

    unittest.main(

        verbosity=2

    )