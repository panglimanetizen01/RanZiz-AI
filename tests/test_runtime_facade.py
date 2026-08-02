"""
RanZiz AI Runtime Facade Test
Version 1.0
"""

import unittest

from source.runtime.facade.runtime_facade import RuntimeFacade


class DummyKernel:


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

        return "runtime response"


    def start(

        self,

        container

    ):

        return "started"


    def stop(

        self

    ):

        return "stopped"



class RuntimeFacadeTest(unittest.TestCase):


    def test_chat(self):

        kernel = DummyKernel()

        facade = RuntimeFacade(
            kernel
        )

        result = facade.chat(
            "halo"
        )

        self.assertEqual(
            result,
            "runtime response"
        )

        self.assertEqual(
            kernel.received[0],
            "halo"
        )


    def test_start_stop(self):

        kernel = DummyKernel()

        facade = RuntimeFacade(
            kernel
        )

        self.assertEqual(
            facade.start(
                {}
            ),
            "started"
        )

        self.assertEqual(
            facade.stop(),
            "stopped"
        )


if __name__ == "__main__":

    unittest.main()