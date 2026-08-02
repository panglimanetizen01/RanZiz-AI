"""
RanZiz AI Test Runner
Version 1.0
"""

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent

if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


def main():

    loader = unittest.TestLoader()

    suite = loader.discover(
        start_dir=str(ROOT / "tests"),
        pattern="test_*.py"
    )

    runner = unittest.TextTestRunner(
        verbosity=2
    )

    result = runner.run(suite)

    print()
    print("=" * 40)
    print("RanZiz AI Test Summary")
    print("=" * 40)
    print(f"Run      : {result.testsRun}")
    print(f"Failures : {len(result.failures)}")
    print(f"Errors   : {len(result.errors)}")

    if result.wasSuccessful():
        print("Status   : SUCCESS")
        return 0

    print("Status   : FAILED")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())