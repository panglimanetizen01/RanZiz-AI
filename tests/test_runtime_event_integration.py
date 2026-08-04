"""
RanZiz AI Runtime Event Integration Test
Version 1.0
"""

from source.capability.capability_planner import CapabilityPlanner
from source.capability.capability_runtime import CapabilityRuntime


class DummyExecutor:

    def __init__(self, name):

        self.name = name

    def execute(self, payload):

        return {
            "result": self.name,
            "status": "ok"
        }


def test_capability_runtime_events():

    planner = CapabilityPlanner()

    runtime = CapabilityRuntime()

    plan = planner.create(
        [
            "Lyric Engine"
        ]
    )

    runtime.execute(
        plan,
        {
            "message": "buat lirik lagu",
            "context": {}
        }
    )

    events = runtime.events.all()

    names = [
        event["event"]
        for event in events
    ]

    assert names[0] == "PLAN_STARTED"

    assert "CAPABILITY_STARTED" in names

    assert "CAPABILITY_COMPLETED" in names

    assert names[-1] == "PLAN_COMPLETED"


def test_capability_runtime_keeps_intelligence_payload():

    planner = CapabilityPlanner()

    runtime = CapabilityRuntime()

    plan = planner.create(
        [
            "Lyric Engine"
        ]
    )

    payload = {
        "message": "buat lagu perjuangan",
        "context": {},
        "intent": "CREATE",
        "goal": "MUSIC",
        "task_type": "general.CREATE"
    }

    runtime.execute(
        plan,
        payload
    )

    assert runtime.snapshot is not None
