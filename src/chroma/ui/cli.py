import argparse

from chroma.domain.model import OutputFormat


def build_parser():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--format",
        choices=[v.value for v in OutputFormat],
        required=False,
    )

    return parser


def parse(args=None) -> argparse.Namespace:
    args = build_parser().parse_args(args)
    return args
