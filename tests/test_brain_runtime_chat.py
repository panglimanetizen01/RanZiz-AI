"""
RanZiz AI Brain Runtime Chat Test
Version 1.0
"""

import unittest

from source.core.brain import Brain


class BrainRuntimeChatTest(unittest.TestCase):


    def test_runtime_exists(self):

        brain = Brain()

        self.assertIsNotNone(
            brain.runtime
        )


    def test_runtime_chat(self):

        brain = Brain()

        result = brain.runtime.process(
            "Halo RanZiz AI"
        )

        self.assertIsNotNone(
            result
        )


    def test_brain_startup(self):

        brain = Brain()

        self.assertIsNotNone(
            brain.startup()
        )


if __name__ == "__main__":

    unittest.main()