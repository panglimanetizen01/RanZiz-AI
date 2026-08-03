"""
RanZiz AI Capability Workflow Chain Test
Version 1.0
"""

import unittest

from source.planner.executor import Executor


class CapabilityWorkflowChainTest(unittest.TestCase):

    def setUp(self):

        self.executor = Executor()


    def test_video_workflow_chain(self):

        result = self.executor.execute(
            {
                "message": "buat video lagu perjuangan",
                "capabilities": [
                    "Video Engine"
                ]
            }
        )

        self.assertEqual(
            result["status"],
            "SUCCESS"
        )

        self.assertIn(
            "Video Engine",
            result["result"]
        )

        self.assertIn(
            "Audio Engine",
            result["result"]
        )


    def test_website_workflow_chain(self):

        result = self.executor.execute(
            {
                "message": "buat website musisi",
                "capabilities": [
                    "Website Engine"
                ]
            }
        )

        self.assertEqual(
            result["status"],
            "SUCCESS"
        )

        self.assertIn(
            "Website Engine",
            result["result"]
        )


    def test_voice_workflow_chain(self):

        result = self.executor.execute(
            {
                "message": "buat narasi sejarah",
                "capabilities": [
                    "Voice Engine"
                ]
            }
        )

        self.assertEqual(
            result["status"],
            "SUCCESS"
        )

        self.assertIn(
            "Voice Engine",
            result["result"]
        )


if __name__ == "__main__":

    unittest.main()
