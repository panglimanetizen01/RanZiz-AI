#!/usr/bin/env python3

from argparse import ArgumentParser

from source.observability.trace_replay import TraceReplay


parser = ArgumentParser()

parser.add_argument(
    "file"
)

group = parser.add_mutually_exclusive_group()

group.add_argument(
    "--retry",
    action="store_true"
)

group.add_argument(
    "--capability",
    action="store_true"
)

group.add_argument(
    "--workflow",
    action="store_true"
)

group.add_argument(
    "--agent",
    action="store_true"
)

args = parser.parse_args()

event_filter = None

if args.retry:
    event_filter = "retry"

elif args.capability:
    event_filter = "capability"

elif args.workflow:
    event_filter = "workflow"

elif args.agent:
    event_filter = "agent"

for line in TraceReplay().replay(
    args.file,
    event_filter
):
    print(line)
