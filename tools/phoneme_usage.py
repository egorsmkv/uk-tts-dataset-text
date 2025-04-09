import polars as pl

df = pl.read_ndjson('tts_dataset.jsonl')

df = df.select([
    pl.col('sentence_phonemized').str.replace_all(r'\s+', '').alias('sentence_phonemized'),
])

# Create a matrix of phoneme usage in the dataset
phoneme_usage = df.select([
    pl.col('sentence_phonemized').str.split('').explode().alias('phoneme'),
]).group_by('phoneme').agg(pl.count()).sort('phoneme')

print(phoneme_usage)
