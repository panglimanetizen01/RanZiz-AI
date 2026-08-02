"""
RanZiz AI Runtime Registry
Version 1.0
"""


from source.core.runtime.brain_runtime_hook import BrainRuntimeHook


class RuntimeRegistry:


    def __init__(self):

        self.runtime = BrainRuntimeHook()



    def get_runtime(self):

        return self.runtime