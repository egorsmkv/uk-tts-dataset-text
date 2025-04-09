"""
git clone https://github.com/patriotyk/ipa-uk
cd ipa-uk
python3 -m pip install .
"""

import polars as pl
from ipa_uk import ipa

df = pl.read_csv('checked_exclamations.csv')
df = df.with_columns(pl.lit('exclamation').alias('type'))

df2 = pl.read_csv('checked_obvious_1.csv')
df2 = df2.with_columns(pl.lit('obvious').alias('type'))

df3 = pl.read_csv('checked_obvious_2.csv')
df3 = df3.with_columns(pl.lit('obvious').alias('type'))

df4 = pl.read_csv('checked_questions.csv')
df4 = df4.with_columns(pl.lit('question').alias('type'))

concat = pl.concat([df, df2, df3, df4])

def count_chars(x):
    return len(x)

def count_word_length(x):
    return len(x.split())

def remove_dashes(v):
    return v.replace('—', '').replace('–', '').strip()

def phonemize(v):
    return ipa(v, check_accent=False)

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

def remove_stresses(x):
    return x.encode('utf-8').replace(b'\xcc\x81', b'').decode('utf-8')

concat = concat.with_columns(pl.col('sentence').alias('sentence_original'))

concat = concat.with_columns(pl.col('sentence').map_elements(remove_dashes, return_dtype=pl.String).alias('sentence'))

concat = concat.with_columns(pl.col('sentence').map_elements(count_word_length, return_dtype=pl.Int64).alias('sentence_word_length'))

concat = concat.with_columns(pl.col('sentence').map_elements(remove_stresses, return_dtype=pl.String).alias('sentence_no_stress'))

concat = concat.with_columns(pl.col('sentence').map_elements(replace_stresses, return_dtype=pl.String).alias('sentence_pluses'))

concat = concat.with_columns(pl.col('sentence_pluses').map_elements(phonemize, return_dtype=pl.String).alias('sentence_pluses_phonemized'))

concat = concat.with_columns(pl.col('sentence_pluses_phonemized').map_elements(count_chars, return_dtype=pl.Int64).alias('sentence_pluses_phonemized_length'))

concat = concat.with_columns(pl.col('sentence_no_stress').map_elements(phonemize, return_dtype=pl.String).alias('sentence_no_stress_phonemized'))

concat = concat.with_columns(pl.col('sentence_no_stress_phonemized').map_elements(count_chars, return_dtype=pl.Int64).alias('sentence_no_stress_phonemized_length'))

concat = concat.with_columns(pl.col('sentence').map_elements(phonemize, return_dtype=pl.String).alias('sentence_phonemized'))

concat = concat.with_columns(pl.col('sentence_phonemized').map_elements(count_chars, return_dtype=pl.Int64).alias('sentence_phonemized_length'))


# Export
concat = concat.select([
    'sentence_original',
    'sentence',
    'sentence_word_length',
    'sentence_phonemized',
    'sentence_phonemized_length',
    'sentence_no_stress',
    'sentence_no_stress_phonemized',
    'sentence_no_stress_phonemized_length',
    'sentence_pluses',
    'sentence_pluses_phonemized',
    'sentence_pluses_phonemized_length',
    'type',
])

print(concat)

concat.write_ndjson('tts_dataset.jsonl')
