"""
RanZiz AI Brain Runtime Hook Test
Version 1.0
"""

import unittest

from source.core.runtime.brain_runtime_hook import (
    BrainRuntimeHook
)


class BrainRuntimeHookTest(unittest.TestCase):


    def test_instance(self):

        hook = BrainRuntimeHook()

        self.assertIsNotNone(
            hook
        )


    def test_execute_connection(self):

        hook = BrainRuntimeHook()

        hook.execute(
            "halo"
        )

        self.assertTrue(
            True
        )


if __name__ == "__main__":

    unittest.main()