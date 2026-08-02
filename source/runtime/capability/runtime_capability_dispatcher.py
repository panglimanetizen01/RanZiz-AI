"""
RanZiz AI Runtime Capability Dispatcher
Version 1.0
"""


class RuntimeCapabilityDispatcher:


    def __init__(

        self,

        registry

    ):

        self.registry = registry


    def dispatch(

        self,

        capability,

        payload=None,

        context=None

    ):

        handler = self.registry.get(

            capability

        )

        if handler is None:

            return None


        if hasattr(

            handler,

            "execute"

        ):

            return handler.execute(

                payload,

                context

            )


        if callable(

            handler

        ):

            return handler(

                payload,

                context

            )


        return handler