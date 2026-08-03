"""
RanZiz AI Capability Loader Test
Version 1.0
"""

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from source.capability.capability_loader import CapabilityLoader


class CapabilityLoaderTest(unittest.TestCase):

    def setUp(self):

        self.loader = CapabilityLoader()

        self.executors = self.loader.load()

    def test_expected_capabilities_exist(self):

        expected = {

            "Lyric Engine",
            "Composer",
            "Audio Engine",
            "Code Engine",
            "Research Engine",
            "Marketing Engine",
            "Image Engine",
            "Website Engine",
            "Video Engine",
            "Document Engine",
            "Vision Engine",
            "Voice Engine",
        }

        loaded = set(self.executors.keys())

        missing = expected - loaded

        self.assertEqual(
            missing,
            set(),
            f"Capability tidak ditemukan: {missing}"
        )

    def test_all_executors_have_required_methods(self):

        for name, executor in self.executors.items():

            self.assertTrue(
                hasattr(executor, "execute"),
                f"{name} tidak memiliki execute()"
            )

            self.assertTrue(
                hasattr(executor, "metadata"),
                f"{name} tidak memiliki metadata()"
            )


if __name__ == "__main__":
    unittest.main(verbosity=2)
