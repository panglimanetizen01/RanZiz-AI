"""
RanZiz AI Capability Plan Contract Test
Version 1.0
"""

from source.capability.capability_plan import CapabilityPlan


class DummyExecutor:
    pass


def test_capability_plan_add_and_names():

    plan = CapabilityPlan()

    plan.add(
        "Composer",
        DummyExecutor(),
        [
            "Lyric Engine"
        ]
    )

    assert len(plan) == 1

    assert plan.names() == [
        "Composer"
    ]

    item = plan.get(
        "Composer"
    )

    assert item["dependencies"] == [
        "Lyric Engine"
    ]

    assert item["status"] == "PENDING"


def test_capability_plan_status_and_result():

    plan = CapabilityPlan()

    plan.add(
        "Lyric Engine",
        DummyExecutor()
    )

    plan.set_status(
        "Lyric Engine",
        "SUCCESS"
    )

    plan.set_result(
        "Lyric Engine",
        {
            "lyrics": "test"
        }
    )

    assert len(plan.completed()) == 1

    assert plan.get(
        "Lyric Engine"
    )["result"]["lyrics"] == "test"
