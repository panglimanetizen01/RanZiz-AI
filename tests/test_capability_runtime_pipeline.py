"""
RanZiz AI Capability Runtime Pipeline Test
Version 1.0
"""

from source.runtime.pipeline.capability_runtime_pipeline import (
    CapabilityRuntimePipeline,
)


def test_capability_runtime_pipeline_execute():

    pipeline = CapabilityRuntimePipeline()

    result = pipeline.execute(
        {
            "message": "buat lagu perjuangan",
            "capabilities": [
                "Lyric Engine"
            ],
            "intent": "CREATE",
            "goal": "MUSIC",
            "task_type": "general.CREATE"
        }
    )

    assert result is not None

    assert "Lyric Engine" in result

    assert result["Lyric Engine"]["status"] == "SUCCESS"


def test_capability_runtime_pipeline_empty_plan():

    pipeline = CapabilityRuntimePipeline()

    result = pipeline.execute(
        None
    )

    assert result is None
