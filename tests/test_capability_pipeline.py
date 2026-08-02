"""
RanZiz AI Capability Pipeline Test
Version 1.0
"""

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from source.capability.pipeline.capability_pipeline import CapabilityPipeline
from source.capability.result.capability_result import CapabilityResult


class DummyExecutor:

    def execute(self, task):

        return CapabilityResult(

            task.capability,

            output=f"OK: {task.capability}"

        )


class CapabilityPipelineTest(unittest.TestCase):

    def setUp(self):

        self.pipeline = CapabilityPipeline(

            DummyExecutor()

        )

    def test_single_capability(self):

        result = self.pipeline.execute(

            ["Lyric Engine"],

            {"message": "Halo"}

        )

        self.assertEqual(

            len(result),

            1

        )

    def test_multiple_capabilities(self):

        result = self.pipeline.execute(

            [

                "Lyric Engine",

                "Composer",

                "Audio Engine"

            ],

            {"message": "buat lagu"}

        )

        self.assertEqual(

            len(result),

            3

        )


if __name__ == "__main__":

    unittest.main(

        verbosity=2

    )