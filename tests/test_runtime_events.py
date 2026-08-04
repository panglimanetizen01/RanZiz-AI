"""
RanZiz AI Runtime Events Test
Version 1.0
"""

from source.runtime.events.runtime_event import RuntimeEvent
from source.runtime.events.runtime_event_bus import RuntimeEventBus


def test_runtime_event():

    event = RuntimeEvent(
        "CAPABILITY_STARTED",
        "Lyric Engine"
    )

    data = event.to_dict()

    assert data["event"] == "CAPABILITY_STARTED"

    assert data["capability"] == "Lyric Engine"



def test_event_bus_emit():

    bus = RuntimeEventBus()

    bus.emit(
        "PLAN_STARTED"
    )

    bus.emit(
        "CAPABILITY_STARTED",
        "Composer"
    )

    bus.emit(
        "CAPABILITY_COMPLETED",
        "Composer",
        {
            "status": "SUCCESS"
        }
    )

    assert len(bus) == 3

    assert bus.all()[0]["event"] == "PLAN_STARTED"

    assert bus.last().event == "CAPABILITY_COMPLETED"



def test_event_bus_clear():

    bus = RuntimeEventBus()

    bus.emit(
        "PLAN_STARTED"
    )

    assert bus.count() == 1

    bus.clear()

    assert bus.count() == 0
