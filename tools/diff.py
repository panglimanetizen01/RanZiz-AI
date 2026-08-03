#!/usr/bin/env python3

import argparse

from source.observability.trace_diff import TraceDiff

parser = argparse.ArgumentParser(
    description="RanZiz AI Trace Diff"
)

parser.add_argument("old")
parser.add_argument("new")

args = parser.parse_args()

result = TraceDiff().compare(
    args.old,
    args.new
)

print("=" * 60)
print("RanZiz AI Trace Diff")
print("=" * 60)

print(f"Status  : {result['status_before']} -> {result['status_after']}")
print(f"Events  : {result['events_before']} -> {result['events_after']}")
print(f"Verdict : {result['verdict']}")
print()

print("Capability Duration")
print("-" * 60)

for capability, data in sorted(result["duration_changes"].items()):
    before = data["before"]
    after = data["after"]

    if before is None:
        delta = "NEW"
    elif after is None:
        delta = "REMOVED"
    else:
        delta = f"{after - before:+.3f}"

    print(
        f"{capability:20} "
        f"{before} ms -> {after} ms "
        f"(Δ {delta})"
    )
