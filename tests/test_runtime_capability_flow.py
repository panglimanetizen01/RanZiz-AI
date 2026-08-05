"""
RanZiz AI Runtime Capability Flow Test
Version 1.0
"""

from source.runtime.builder.runtime_builder import RuntimeBuilder


def test_runtime_capability_pipeline_flow():

    builder = RuntimeBuilder()

    runtime = builder.build()

    result = runtime.process(
        "buat lagu dangdut tentang perjuangan",
        {
            "plan": {
                "message": "buat lagu dangdut tentang perjuangan",
                "capabilities": [
                    "Lyric Engine"
                ],
                "intent": "CREATE",
                "goal": "MUSIC",
                "task_type": "general.CREATE"
            }
        }
    )

    assert result is not None

    assert result.capability == "Lyric Engine"
    assert result.status == "SUCCESS"

    assert result.capability == "Lyric Engine"
    assert result.status == "SUCCESS"



def test_runtime_fallback_without_plan():

    builder = RuntimeBuilder()

    runtime = builder.build()

    result = runtime.process(
        "halo",
        {}
    )

    assert result is not None
