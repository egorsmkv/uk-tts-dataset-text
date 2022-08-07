from ukrainian_accentor_transformer import Accentor
import argparse


def pluses_to_accents(x: str):
    chars = list(x)

    idx = -1
    final_chars = []
    for i, c in enumerate(chars):
        if c == '+':
            idx = i
        else:
            if idx != -1:
                final_chars.append(c.encode('utf-8'))
                final_chars.append(b'\xcc\x81')
                idx = -1
            else:
                final_chars.append(c.encode('utf-8'))

    return ''.join([c.decode('utf-8') for c in final_chars])


def run(in_file):
    # Read files
    with open(in_file) as h:
        lines = [it.strip() for it in h.readlines()]

    accentor = Accentor('cuda')

    print('sentence')
    for line in lines:
        try:
            if not line.endswith('!') and not line.endswith('?'):
                line = line + '.'
            line_stressed = accentor([line])[0]
            print('"' + pluses_to_accents(line_stressed) + '"')
        except Exception:
            pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Tool to add stresses to file lines."
    )
    parser.add_argument(
        "--in_file", help="Path to input file", type=str, required=True
    )
    args = parser.parse_args()

    run(args.in_file)

