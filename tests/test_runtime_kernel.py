"""
RanZiz AI Runtime Kernel Test
Version 1.0
"""

import unittest

from source.runtime.kernel.runtime_kernel import RuntimeKernel


class DummyRuntime:


    def __init__(self):

        self.received = None


    def process(

        self,

        message,

        context=None

    ):

        self.received = (

            message,

            context

        )

        return "kernel response"



    def start(

        self,

        container

    ):

        return "started"



    def stop(

        self

    ):

        return "stopped"



class DummyProvider:


    def __init__(

        self

    ):

        self.runtime = DummyRuntime()



    def get(

        self

    ):

        return self.runtime



class RuntimeKernelTest(unittest.TestCase):


    def test_process(self):

        provider = DummyProvider()

        kernel = RuntimeKernel(
            provider
        )

        result = kernel.process(
            "halo"
        )

        self.assertEqual(
            result,
            "kernel response"
        )


        self.assertEqual(
            provider.runtime.received[0],
            "halo"
        )



    def test_start_stop(self):

        provider = DummyProvider()

        kernel = RuntimeKernel(
            provider
        )

        self.assertEqual(
            kernel.start(
                {}
            ),
            "started"
        )


        self.assertEqual(
            kernel.stop(),
            "stopped"
        )



if __name__ == "__main__":

    unittest.main()