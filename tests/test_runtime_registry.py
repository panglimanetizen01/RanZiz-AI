"""
RanZiz AI Runtime Registry Test
Version 1.0
"""

import unittest

from source.core.runtime.runtime_registry import RuntimeRegistry


class RuntimeRegistryTest(unittest.TestCase):


    def test_instance(self):

        registry = RuntimeRegistry()

        self.assertIsNotNone(
            registry
        )


    def test_get_runtime(self):

        registry = RuntimeRegistry()

        runtime = registry.get_runtime()

        self.assertIsNotNone(
            runtime
        )


    def test_runtime_execute_exists(self):

        registry = RuntimeRegistry()

        runtime = registry.get_runtime()

        self.assertTrue(
            hasattr(
                runtime,
                "execute"
            )
        )


if __name__ == "__main__":

    unittest.main()