"""
RanZiz AI Workflow Router Test
Version 2.0
"""

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from source.workflow.workflow_router import WorkflowRouter


class DummyWorkflow:

    def run(self, message):

        return f"WORKFLOW: {message}"


class DummyAgent:

    def execute(self, message, context=None):

        return f"AGENT: {message}"


class WorkflowRouterTest(unittest.TestCase):

    def setUp(self):

        self.router = WorkflowRouter(
            DummyWorkflow(),
            DummyAgent()
        )

    def test_music_request(self):

        result = self.router.execute(
            "buat lagu dangdut tentang perjuangan"
        )

        self.assertIsNotNone(result)

    def test_chat_request(self):

        result = self.router.execute(
            "Halo"
        )

        self.assertIsNotNone(result)


if __name__ == "__main__":
    unittest.main(verbosity=2)