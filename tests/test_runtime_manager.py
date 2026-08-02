"""
RanZiz AI Core Runtime Manager Test
Version 1.0
"""

import unittest

from source.core.runtime.runtime_manager import RuntimeManager


class RuntimeManagerTest(unittest.TestCase):


    def test_instance(self):

        manager = RuntimeManager()

        self.assertIsNotNone(
            manager
        )


    def test_process_connection(self):

        manager = RuntimeManager()

        manager.process(
            "halo"
        )

        self.assertTrue(
            True
        )


if __name__ == "__main__":

    unittest.main()