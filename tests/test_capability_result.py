"""
RanZiz AI Capability Result Contract Test
Version 1.0
"""

import sys
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parent.parent

if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from source.capability.result.capability_result import CapabilityResult


class CapabilityResultTest(unittest.TestCase):

    def test_to_dict_contract(self):

        result = CapabilityResult(
            "Lyric Engine",
            status="SUCCESS",
            output={
                "lyrics": "test"
            },
            metadata={
                "version": 1
            }
        )

        data = result.to_dict()

        self.assertEqual(
            data["capability"],
            "Lyric Engine"
        )

        self.assertEqual(
            data["status"],
            "SUCCESS"
        )

        self.assertEqual(
            data["output"]["lyrics"],
            "test"
        )

        self.assertEqual(
            data["metadata"]["version"],
            1
        )


    def test_default_metadata_contract(self):

        result = CapabilityResult(
            "Composer"
        )

        self.assertEqual(
            result.status,
            "SUCCESS"
        )

        self.assertEqual(
            result.metadata,
            {}
        )


if __name__ == "__main__":

    unittest.main(
        verbosity=2
    )
