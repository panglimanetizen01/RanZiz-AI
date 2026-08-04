"""
RanZiz AI Capability Dependency Contract Test
Version 1.0
"""

import sys
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parent.parent

if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from source.capability.capability_router import CapabilityRouter
from source.capability.dependency.capability_dependency_resolver import (
    CapabilityDependencyResolver,
)


class CapabilityDependencyTest(unittest.TestCase):

    def setUp(self):

        router = CapabilityRouter()

        self.resolver = CapabilityDependencyResolver(
            router.registry
        )


    def test_dependency_order(self):

        result = self.resolver.resolve(
            [
                "Audio Engine"
            ]
        )

        self.assertEqual(
            result,
            [
                "Lyric Engine",
                "Composer",
                "Audio Engine"
            ]
        )


    def test_duplicate_dependency_removed(self):

        result = self.resolver.resolve(
            [
                "Composer",
                "Audio Engine"
            ]
        )

        self.assertEqual(
            result.count("Composer"),
            1
        )


if __name__ == "__main__":

    unittest.main(
        verbosity=2
    )
