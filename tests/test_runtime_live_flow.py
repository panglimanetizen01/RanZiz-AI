"""
RanZiz AI Runtime Live Flow Test
Version 1.0
"""

import unittest

from source.core.runtime.runtime_adapter import RuntimeAdapter


class RuntimeLiveFlowTest(unittest.TestCase):


    def test_runtime_flow(self):

        runtime = RuntimeAdapter()

        result = runtime.process(
            "halo"
        )

        self.assertIsNotNone(
            result
        )


if __name__ == "__main__":

    unittest.main()