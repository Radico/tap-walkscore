from tap_kit import main_method
from tap_kit import BaseClient

from .score import ScoreStream
from .executor import WalkScoreExecutor


REQUIRED_CONFIG_KEYS = [
    "wsapikey",
    "locations",
]

STREAMS = [
    ScoreStream,
]


def main():
    main_method(
        REQUIRED_CONFIG_KEYS,
        WalkScoreExecutor,
        BaseClient,
        STREAMS
    )


if __name__ == '__main__':
    main()
