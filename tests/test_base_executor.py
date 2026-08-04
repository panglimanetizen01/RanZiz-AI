"""
RanZiz AI Base Capability Executor Test
Version 1.0
"""

import sys
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parent.parent

if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from source.capability.base_executor import BaseCapabilityExecutor


class DummyExecutor(BaseCapabilityExecutor):

    def execute(self, payload):

        return self.success(
            {
                "echo": payload
            }
        )

    def metadata(self):

        return None


class BaseExecutorTest(unittest.TestCase):

    def setUp(self):

        self.executor = DummyExecutor()


    def test_success_contract(self):

        result = self.executor.execute(
            {
                "message": "hello"
            }
        )

        self.assertEqual(
            result["status"],
            "SUCCESS"
        )

        self.assertIn(
            "capability",
            result
        )

        self.assertIn(
            "data",
            result
        )


    def test_failure_contract(self):

        result = self.executor.failure(
            "error"
        )

        self.assertEqual(
            result["status"],
            "FAILED"
        )

        self.assertEqual(
            result["error"],
            "error"
        )


if __name__ == "__main__":

    unittest.main(
        verbosity=2
    )
