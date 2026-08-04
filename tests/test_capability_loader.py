"""
RanZiz AI Capability Loader Test
Version 1.0
"""

import sys
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parent.parent

if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from source.capability.capability_loader import CapabilityLoader
from source.capability.schema.capability_info import CapabilityInfo


class CapabilityLoaderTest(unittest.TestCase):

    def setUp(self):

        self.loader = CapabilityLoader()


    def test_load_with_metadata_contract(self):

        result = self.loader.load_with_metadata()

        self.assertIsInstance(
            result,
            dict
        )

        self.assertGreater(
            len(result),
            0
        )

        for name, item in result.items():

            self.assertIn(
                "executor",
                item
            )

            self.assertIn(
                "info",
                item
            )

            self.assertTrue(
                hasattr(
                    item["executor"],
                    "execute"
                )
            )

            self.assertIsInstance(
                item["info"],
                CapabilityInfo
            )

            self.assertEqual(
                item["info"].name,
                name
            )


if __name__ == "__main__":

    unittest.main(
        verbosity=2
    )
