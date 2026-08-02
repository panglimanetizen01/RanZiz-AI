"""
RanZiz AI Core Runtime Adapter Test
Version 1.0
"""

import unittest

from source.core.runtime.core_runtime_adapter import CoreRuntimeAdapter


class CoreRuntimeAdapterTest(unittest.TestCase):

    def test_instance(self):

        adapter = CoreRuntimeAdapter()

        self.assertIsNotNone(adapter)


    def test_process_connection(self):

        adapter = CoreRuntimeAdapter()

        adapter.process(
            "halo"
        )

        self.assertTrue(True)


if __name__ == "__main__":

    unittest.main()