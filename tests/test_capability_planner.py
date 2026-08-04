"""
RanZiz AI Capability Planner Contract Test
Version 1.0
"""

from source.capability.capability_planner import CapabilityPlanner


def test_capability_planner_create_dependency_order():

    planner = CapabilityPlanner()

    plan = planner.create(
        [
            "Audio Engine"
        ]
    )

    assert plan.names() == [
        "Lyric Engine",
        "Composer",
        "Audio Engine"
    ]


def test_capability_planner_executor_contract():

    planner = CapabilityPlanner()

    plan = planner.create(
        [
            "Lyric Engine"
        ]
    )

    item = plan.get(
        "Lyric Engine"
    )

    assert item is not None

    assert hasattr(
        item["executor"],
        "execute"
    )

    assert hasattr(
        item["executor"],
        "metadata"
    )
