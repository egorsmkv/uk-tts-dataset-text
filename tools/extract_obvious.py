import re
import argparse

MIN_LEN = 10
MAX_LEN = 80

def count_words(line):
    return len(line.split(' '))

def has_cyrillic(text):
    return bool(re.search('[а-яА-Я]', text))


def run(in_file):
    # Read files
    with open(in_file) as h:
        lines = [it.strip() for it in h.readlines()]

    for line in lines:
        sentences = [it.strip() for it in line.split('.')]
        sentences = [it for it in sentences if count_words(it) > 2]

        # predicate
        sentences = [it for it in sentences if not it.endswith('!') and not it.endswith('?')]

        sentences = [it for it in sentences if len(it) < MAX_LEN and len(it) > MIN_LEN]
        
        if not sentences:
            continue
        
        for sentence in list(set(sentences)):
            if any(elem in sentence for elem in  ['[', ']', '&', '*', ';', '…']):
                continue
            if not has_cyrillic(sentence):
                continue
            print(sentence)



if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Tool to extract only sentences with ? mark."
    )
    parser.add_argument(
        "--in_file", help="Path to input file", type=str, required=True
    )
    args = parser.parse_args()

    run(args.in_file)

