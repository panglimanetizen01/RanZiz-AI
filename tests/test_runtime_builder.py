"""
RanZiz AI Runtime Builder Test
Version 1.1
"""

import unittest

from source.runtime.builder.runtime_builder import (
    RuntimeBuilder
)


class RuntimeBuilderTest(unittest.TestCase):


    def test_build(self):

        builder = RuntimeBuilder()

        runtime = builder.build()

        self.assertIsNotNone(
            runtime
        )


    def test_runtime_bridge_interface(self):

        builder = RuntimeBuilder()

        runtime = builder.build()

        self.assertTrue(
            hasattr(
                runtime,
                "process"
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