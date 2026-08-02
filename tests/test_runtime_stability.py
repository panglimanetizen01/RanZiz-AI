"""
RanZiz AI Runtime Stability Test
Version 1.0
"""

import unittest

from source.core.runtime.runtime_adapter import RuntimeAdapter


class RuntimeStabilityTest(unittest.TestCase):


    def test_multiple_requests(self):

        runtime = RuntimeAdapter()

        messages = [

            "Halo",

            "Apa kabar?",

            "Siapa kamu?",

            "Tes Runtime",

            "RanZiz AI"

        ]


        for message in messages:

            result = runtime.process(
                message
            )

            self.assertIsNotNone(
                result
            )


    def test_runtime_reuse(self):

        runtime = RuntimeAdapter()

        first = runtime.process(
            "Halo"
        )

        second = runtime.process(
            "Halo lagi"
        )

        self.assertIsNotNone(
            first
        )

        self.assertIsNotNone(
            second
        )


if __name__ == "__main__":

    unittest.main()