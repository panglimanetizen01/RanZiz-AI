"""
RanZiz AI Runtime Composition Test
Version 1.1
"""

import unittest

from source.runtime.composition.runtime_composition_root import (
    RuntimeCompositionRoot
)


class RuntimeCompositionTest(unittest.TestCase):


    def test_instance(self):

        root = RuntimeCompositionRoot()

        self.assertIsNotNone(
            root
        )


    def test_get_runtime(self):

        root = RuntimeCompositionRoot()

        runtime = root.get_runtime()

        self.assertIsNotNone(
            runtime
        )


    def test_runtime_interface(self):

        root = RuntimeCompositionRoot()

        runtime = root.get_runtime()

        self.assertTrue(
            hasattr(
                runtime,
                "chat"
            )
        )

        self.assertTrue(
            hasattr(
                runtime,
                "start"
            )
        )

        self.assertTrue(
            hasattr(
                runtime,
                "stop"
            )
        )


if __name__ == "__main__":

    unittest.main()