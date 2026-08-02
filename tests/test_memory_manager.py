"""
RanZiz AI Memory Manager Test
Version 2.0
"""

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from source.memory.manager.memory_manager import (
    MemoryManager
)


class MemoryManagerTest(unittest.TestCase):

    def setUp(self):

        self.memory = MemoryManager()

    def test_instance(self):

        self.assertIsNotNone(
            self.memory
        )

    def test_save(self):

        result = self.memory.save(
            "unit_test",
            {
                "value": "hello"
            }
        )

        self.assertIsNotNone(
            result
        )

    def test_exists(self):

        self.memory.save(
            "exists_test",
            {
                "value": 123
            }
        )

        self.assertTrue(
            self.memory.exists(
                "exists_test"
            )
        )

    def test_get(self):

        self.memory.save(
            "get_test",
            "RanZiz"
        )

        self.assertEqual(
            self.memory.get(
                "get_test"
            ),
            "RanZiz"
        )

    def test_all(self):

        memories = self.memory.all()

        self.assertIsInstance(
            memories,
            dict
        )

    def test_consolidate(self):

        result = self.memory.consolidate()

        self.assertIsNotNone(
            result
        )


if __name__ == "__main__":
    unittest.main(
        verbosity=2
    )