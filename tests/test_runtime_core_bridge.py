"""
RanZiz AI Runtime Core Bridge Test
Version 1.0
"""

import unittest

from source.core.bridge.runtime_core_bridge import (
    RuntimeCoreBridge
)


class DummyGateway:


    def __init__(self):

        self.message = None



    def process(

        self,

        message,

        context=None

    ):

        self.message = message

        return "bridge response"



    def start(

        self,

        container

    ):

        return "started"



    def stop(

        self

    ):

        return "stopped"



class RuntimeCoreBridgeTest(unittest.TestCase):


    def test_process(self):

        gateway = DummyGateway()

        bridge = RuntimeCoreBridge(
            gateway
        )

        result = bridge.process(
            "halo"
        )

        self.assertEqual(
            result,
            "bridge response"
        )

        self.assertEqual(
            gateway.message,
            "halo"
        )



    def test_lifecycle(self):

        gateway = DummyGateway()

        bridge = RuntimeCoreBridge(
            gateway
        )

        self.assertEqual(
            bridge.start(
                {}
            ),
            "started"
        )


        self.assertEqual(
            bridge.stop(),
            "stopped"
        )


if __name__ == "__main__":

    unittest.main()