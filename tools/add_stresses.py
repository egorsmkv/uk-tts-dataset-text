import argparse
from ukrainian_word_stress import Stressifier, StressSymbol


def replace_stresses(x):
    chars = list(x.encode('utf-8').replace(b'\xcc\x81', b'+').decode('utf-8'))

    final_chars = []
    for i, c in enumerate(chars):
        if c == '+':
            try:
                tmp = final_chars[i - 1]

                final_chars.pop()
                final_chars.append('+')
                final_chars.append(tmp)
            except IndexError:
                final_chars.append(c)
        else:
            final_chars.append(c)

    return ''.join(final_chars)


def run(in_file):
    # Read files
    with open(in_file) as h:
        lines = [it.strip() for it in h.readlines()]

    # Init stressifier
    stressify = Stressifier(stress_symbol=StressSymbol.CombiningAcuteAccent)

    for line in lines:
        line_stressed = stressify(line)
        plused_stress = replace_stresses(line_stressed)
        print(line + '|' + line_stressed + '|' + plused_stress)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Tool to add stresses to file lines."
    )
    parser.add_argument(
        "--in_file", help="Path to input file", type=str, required=True
    )
    args = parser.parse_args()

    run(args.in_file)

