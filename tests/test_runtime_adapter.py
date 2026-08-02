"""
RanZiz AI Runtime Adapter Test
Version 1.0
"""

import unittest

from source.core.runtime.core_runtime_adapter import CoreRuntimeAdapter


class DummyRuntime:


    def __init__(self):

        self.message = None



    def chat(

        self,

        message,

        context=None

    ):

        self.message = message

        return "adapter response"



class RuntimeAdapterTest(unittest.TestCase):


    def test_process(self):

        adapter = CoreRuntimeAdapter()

        adapter.runtime = DummyRuntime()


        result = adapter.process(
            "halo"
        )


        self.assertEqual(
            result,
            "adapter response"
        )


        self.assertEqual(
            adapter.runtime.message,
            "halo"
        )


if __name__ == "__main__":

    unittest.main()