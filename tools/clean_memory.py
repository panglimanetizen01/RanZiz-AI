"""
RanZiz AI Memory Cleaner
Version 1.1
"""

import json
import sys
from pathlib import Path

# Tambahkan root project ke Python path
ROOT = Path(__file__).resolve().parent.parent

if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from source.config.config import Config


def normalize(item):

    if not isinstance(item, dict):

        return {
            "type": "unknown",
            "source": "unknown",
            "user": str(item),
            "assistant": ""
        }

    if "assistant" in item:

        return {
            "type": item.get("type", "chat"),
            "source": item.get("source", "unknown"),
            "user": item.get("user", ""),
            "assistant": item.get("assistant", "")
        }

    if "ai" in item:

        return {
            "type": "chat",
            "source": "legacy",
            "user": item.get("user", ""),
            "assistant": item.get("ai", "")
        }

    return {
        "type": item.get("type", "chat"),
        "source": item.get("source", "unknown"),
        "user": item.get("user", ""),
        "assistant": item.get("assistant", "")
    }


def main():

    memory_file = Path(Config.MEMORY_FILE)

    if not memory_file.exists():

        print("Memory file tidak ditemukan.")
        return

    try:

        with memory_file.open(
            "r",
            encoding="utf-8"
        ) as file:

            history = json.load(file)

    except Exception as e:

        print(f"Gagal membaca memory: {e}")
        return

    cleaned = []

    seen = set()

    for item in history:

        item = normalize(item)

        key = (
            item.get("type"),
            item.get("source"),
            item.get("user"),
            item.get("assistant")
        )

        if key in seen:
            continue

        seen.add(key)

        cleaned.append(item)

    with memory_file.open(
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            cleaned,
            file,
            ensure_ascii=False,
            indent=4
        )

    print("========================================")
    print("RanZiz AI Memory Cleaner")
    print("========================================")
    print(f"Sebelum : {len(history)}")
    print(f"Sesudah : {len(cleaned)}")
    print(f"Dihapus : {len(history) - len(cleaned)}")


if __name__ == "__main__":

    main()