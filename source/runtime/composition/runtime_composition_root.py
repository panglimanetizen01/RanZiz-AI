"""
RanZiz AI Runtime Composition Root
Version 1.0
"""


from source.runtime.facade.runtime_facade import RuntimeFacade
from source.runtime.kernel.runtime_kernel import RuntimeKernel
from source.runtime.provider.runtime_provider import RuntimeProvider


class RuntimeCompositionRoot:


    def __init__(

        self

    ):

        self.provider = RuntimeProvider()

        self.kernel = RuntimeKernel(

            self.provider

        )

        self.facade = RuntimeFacade(

            self.kernel

        )



    def get_runtime(

        self

    ):

        return self.facade