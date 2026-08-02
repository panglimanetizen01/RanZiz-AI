"""
RanZiz AI Runtime Wiring Test
Version 1.0
"""

import unittest

from source.runtime.composition.runtime_composition_root import (
    RuntimeCompositionRoot
)


class RuntimeWiringTest(unittest.TestCase):


    def test_runtime_creation(self):

        root = RuntimeCompositionRoot()

        runtime = root.get_runtime()

        self.assertIsNotNone(
            runtime
        )


    def test_runtime_methods(self):

        root = RuntimeCompositionRoot()

        runtime = root.get_runtime()

        self.assertTrue(
            hasattr(runtime, "chat")
        )

        self.assertTrue(
            hasattr(runtime, "start")
        )

        self.assertTrue(
            hasattr(runtime, "stop")
        )



if __name__ == "__main__":

    unittest.main()