"""Command-line interface for SacraScript Medieval."""
import argparse
from .generator import generate


def build_parser():
    parser = argparse.ArgumentParser(
        prog="sacrascript",
        description="Draft medieval-inspired Christian texts (not official liturgical forms).",
    )
    parser.add_argument("--kind", choices=("prayer", "blessing", "sermon", "blog"), required=True)
    parser.add_argument("--occasion", required=True, help="Theme, e.g. peace, harvest, mercy.")
    parser.add_argument("--language", choices=("latin", "polish", "bilingual"), default="polish")
    parser.add_argument("--audience", default="parish")
    parser.add_argument("--title", default=None)
    return parser


def main():
    args = build_parser().parse_args()
    print(generate(args.kind, args.occasion, args.language, args.audience, args.title))
    print("\n[Uwaga: współczesna stylizacja inspirowana epoką ok. 1400 r.; nie jest to "
          "potwierdzone źródło historyczne ani zatwierdzony tekst liturgiczny.]")
