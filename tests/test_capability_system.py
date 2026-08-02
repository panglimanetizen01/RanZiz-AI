"""
RanZiz AI Capability System Test
Version 1.1
"""

import sys
from pathlib import Path

sys.path.insert(
    0,
    str(Path(__file__).parent.parent)
)


from source.capability.capability_registry import CapabilityRegistry
from source.capability.capability_executor import CapabilityExecutor
from source.capability.executors.lyric_executor import LyricExecutor
from source.tasks.task import Task


registry = CapabilityRegistry()


registry.register(
    "Lyric Engine",
    LyricExecutor()
)


executor = CapabilityExecutor(
    registry
)


task = Task(
    "Lyric Engine",
    capability="Lyric Engine",
    payload={
        "message": "buat lagu dangdut tentang perjuangan"
    }
)


result = executor.execute(
    task
)


print(result)

print(
    task.info()
)