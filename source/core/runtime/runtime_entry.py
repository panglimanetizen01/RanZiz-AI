"""
RanZiz AI Runtime Entry
Version 2.0
"""

from source.core.runtime.runtime_manager import RuntimeManager


class RuntimeEntry:

    def __init__(self):
        self.manager = RuntimeManager()

    # ==========================================
    # Compatibility Layer
    # ==========================================

    def process(
        self,
        message,
        context=None
    ):
        return self.manager.process(
            message,
            context
        )

    def execute(
        self,
        message,
        context=None
    ):
        return self.process(
            message,
            context
        )

    # ==========================================

    def start(
        self,
        container
    ):
        return self.manager.start(
            container
        )

    def stop(self):
        return self.manager.stop()
