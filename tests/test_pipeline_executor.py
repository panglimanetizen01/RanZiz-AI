"""
RanZiz AI Pipeline Executor Test
Version 1.0
"""

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from source.planner.pipeline_executor import PipelineExecutor
from source.capability.result.capability_result import CapabilityResult


class DummyCapabilityExecutor:

    def execute(self, task):

        return CapabilityResult(

            task.capability,

            output=f"Executed: {task.capability}"

        )


class PipelineExecutorTest(unittest.TestCase):

    def setUp(self):

        self.executor = PipelineExecutor(

            DummyCapabilityExecutor()

        )

    def test_single_capability(self):

        plan = {

            "topic": "buat lagu",

            "capabilities": [

                "Lyric Engine"

            ]

        }

        result = self.executor.execute(

            plan

        )

        self.assertEqual(

            len(result),

            1

        )

    def test_multiple_capabilities(self):

        plan = {

            "topic": "buat lagu",

            "capabilities": [

                "Lyric Engine",

                "Composer",

                "Audio Engine"

            ]

        }

        result = self.executor.execute(

            plan

        )

        self.assertEqual(

            len(result),

            3

        )


if __name__ == "__main__":

    unittest.main(

        verbosity=2

    )