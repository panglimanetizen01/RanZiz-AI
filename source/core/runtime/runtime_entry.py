"""
RanZiz AI Runtime Entry
Version 2.1
"""

from source.core.runtime.runtime_manager import RuntimeManager


class RuntimeEntry:

    def __init__(self):
        self.manager = RuntimeManager()

    # ==========================================
    # Core Runtime API
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
    # Legacy Compatibility Layer
    # ==========================================

    def ask(
        self,
        message
    ):
        return self.process(
            message
        )

    def ask_with_provider(
        self,
        provider,
        message
    ):
        return self.process(
            message,
            {
                "provider": provider
            }
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
