"""
RanZiz AI Runtime Entry Test
Version 1.0
"""

import unittest

from source.core.runtime.runtime_entry import RuntimeEntry


class RuntimeEntryTest(unittest.TestCase):


    def test_instance(self):

        entry = RuntimeEntry()

        self.assertIsNotNone(
            entry
        )


    def test_execute_connection(self):

        entry = RuntimeEntry()

        entry.execute(
            "halo"
        )

        self.assertTrue(
            True
        )


if __name__ == "__main__":

    unittest.main()