import polars as pl

df = pl.read_ndjson('tts_dataset.jsonl')

chars = df['sentence_phonemized']

texts = ' '.join(chars)
unique_chars = set(list(''.join(chars)))

print(len(unique_chars), unique_chars)
