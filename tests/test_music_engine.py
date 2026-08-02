"""
RanZiz AI Music Engine Test
Version 1.0
"""

from source.engines.music import MusicEngine


def main():

    engine = MusicEngine()

    request = {

        "action": "CREATE",

        "goal": "MUSIC",

        "topic": "IBU",

        "emotion": "SAD"

    }

    result = engine.run(None, request)

    print("=" * 40)
    print("RanZiz AI Music Engine Test")
    print("=" * 40)

    print("\nMetadata:")
    for key, value in result["metadata"].items():
        print(f"{key}: {value}")

    print("\nLyrics:")
    print(result["lyrics"])


if __name__ == "__main__":
    main()