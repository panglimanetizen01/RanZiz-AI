"""
RanZiz AI Runtime Real Chat Test
Version 1.0
"""

import unittest

from source.core.runtime.core_runtime_adapter import CoreRuntimeAdapter


class RuntimeRealChatTest(unittest.TestCase):


    def test_chat_returns_value(self):

        runtime = CoreRuntimeAdapter()

        result = runtime.process(
            "Apa kabar?"
        )

        self.assertTrue(
            result is not None
        )


    def test_chat_type(self):

        runtime = CoreRuntimeAdapter()

        result = runtime.process(
            "Halo"
        )

        self.assertTrue(
            isinstance(
                result,
                (
                    str,
                    dict,
                    list
                )
            )
        )


if __name__ == "__main__":

    unittest.main()