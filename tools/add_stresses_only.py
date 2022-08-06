import argparse
from ukrainian_word_stress import Stressifier, StressSymbol


def run(in_file):
    # Read files
    with open(in_file) as h:
        lines = [it.strip() for it in h.readlines()]

    # Init stressifier
    stressify = Stressifier(stress_symbol=StressSymbol.CombiningAcuteAccent)

    for line in lines:
        line_stressed = stressify(line)
        print(line_stressed)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Tool to add stresses to file lines."
    )
    parser.add_argument(
        "--in_file", help="Path to input file", type=str, required=True
    )
    args = parser.parse_args()

    run(args.in_file)

