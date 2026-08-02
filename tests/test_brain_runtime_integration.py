"""
RanZiz AI Brain Runtime Integration Test
Version 1.0
"""

import unittest

from source.core.brain import Brain


class BrainRuntimeIntegrationTest(unittest.TestCase):


    def test_runtime_exists(self):

        brain = Brain()

        self.assertIsNotNone(
            brain.runtime
        )


    def test_runtime_hook_exists(self):

        brain = Brain()

        self.assertTrue(
            hasattr(
                brain.runtime,
                "execute"
            )
        )


if __name__ == "__main__":

    unittest.main()