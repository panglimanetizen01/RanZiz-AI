"""
RanZiz AI Runtime Music Chain Test
Version 1.0
"""

from source.runtime.builder.runtime_builder import RuntimeBuilder


def test_runtime_music_dependency_chain():

    builder = RuntimeBuilder()

    runtime = builder.build()

    result = runtime.process(
        "buat lagu dangdut tentang perjuangan",
        {
            "plan": {
                "message": "buat lagu dangdut tentang perjuangan",
                "capabilities": [
                    "Audio Engine"
                ],
                "intent": "CREATE",
                "goal": "MUSIC",
                "task_type": "general.CREATE"
            }
        }
    )

    assert result is not None

    assert "Lyric Engine" in result

    assert "Composer" in result

    assert "Audio Engine" in result


def test_runtime_music_results_are_success():

    builder = RuntimeBuilder()

    runtime = builder.build()

    result = runtime.process(
        "buat lagu",
        {
            "plan": {
                "message": "buat lagu",
                "capabilities": [
                    "Audio Engine"
                ]
            }
        }
    )

    for name in [
        "Lyric Engine",
        "Composer",
        "Audio Engine"
    ]:
        assert result[name]["status"] == "SUCCESS"
