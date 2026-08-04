from source.runtime.state.runtime_state import RuntimeState


def test_runtime_state_flow():

    state = RuntimeState()

    assert state.is_state(
        "CREATED"
    )

    state.transition(
        "PLANNING"
    )

    state.transition(
        "RUNNING"
    )

    state.transition(
        "COMPLETED"
    )

    assert state.current == "COMPLETED"

    assert state.all() == [
        "CREATED",
        "PLANNING",
        "RUNNING",
        "COMPLETED",
    ]


def test_runtime_state_invalid():

    state = RuntimeState()

    try:

        state.transition(
            "UNKNOWN"
        )

        assert False

    except ValueError:

        assert True
