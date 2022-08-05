import argparse
import re

MIN_LEN = 10
MAX_LEN = 80

def count_words(line):
    return len(line.split(' '))

def only_uk_sentence(v):
    char_set_lower = 'а, б, в, г, ґ, д, е, є, ж, з, и, і, ї, й, к, л, м, н, о, п, р, с, т, у, ф, х, ц, ч, ш, щ, ь, ю, я'.replace(',','').replace(' ', '')
    char_set_upper = char_set_lower.upper()
    char_set = char_set_lower + char_set_upper
    char_set = char_set + '—,!?' + "'" + ' '

    return all((True if x in char_set else False for x in v))


def run(in_file):
    # Read files
    with open(in_file) as h:
        lines = [it.strip() for it in h.readlines()]

    for line in lines:
        sentences = [it.strip() for it in line.split('.')]
        sentences = [it for it in sentences if count_words(it) > 2]

        # predicate
        sentences = [it for it in sentences if it.endswith('!')]

        sentences = [it for it in sentences if len(it) < MAX_LEN and len(it) > MIN_LEN]
        
        if not sentences:
            continue
            
        for sentence in list(set(sentences)):
            if any(elem in sentence for elem in  ['[', ']', '&', '*', ';', '…']):
                continue
            if not only_uk_sentence(sentence):
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

