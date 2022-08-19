import argparse


def run(in_file):
    # Read files
    with open(in_file) as h:
        lines = [it.strip() for it in h.readlines()]

    print('n,orig_text_wo_stress,orig_text')
    
    for n, l in enumerate(lines[1:]):
        orig_text_wo_stress = ''.join(list(l.encode('utf-8').replace(b'\xcc\x81', b'').decode('utf-8')))
        orig_text = l

        print(f'{n},{orig_text_wo_stress},{orig_text}')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Tool to add generate a CSV file used in the Online Microphone application"
    )
    parser.add_argument(
        "--in_file", help="Path to input file", type=str, required=True
    )
    args = parser.parse_args()

    run(args.in_file)

