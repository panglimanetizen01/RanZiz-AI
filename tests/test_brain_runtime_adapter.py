"""
RanZiz AI Brain Runtime Adapter Test
Version 1.0
"""

import unittest

from source.core.brain import Brain


class BrainRuntimeAdapterTest(unittest.TestCase):


    def test_brain_has_runtime(self):

        brain = Brain()

        self.assertIsNotNone(
            brain.runtime
        )


    def test_runtime_process_exists(self):

        brain = Brain()

        self.assertTrue(
            hasattr(
                brain.runtime,
                "process"
            )
        )


if __name__ == "__main__":

    unittest.main()