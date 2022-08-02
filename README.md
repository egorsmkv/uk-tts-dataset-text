# Texts for Ukrainian Text to Speech dataset

## Overview

This repository contains scripts to generate TTS datasets for Ukrainian.

## Install

```bash
pip install ukrainian-word-stress
```

## Data

It is in the `data/raw` folder.

## Apply scripts to data

### Extract appropriate sentences

```bash
python tools/extract_exclamations.py --in_file data/raw/chorna_rada.txt

python tools/extract_questions.py --in_file data/raw/chorna_rada.txt

python tools/extract_lines.py --in_file data/raw/chorna_rada.txt
```

### Add stresses

```bash
python tools/add_stresses.py --in_file datasets/unstressed.txt >> datasets/stressed.txt
```

## Acknowledgements

- Ukrainian word stress: https://github.com/lang-uk/ukrainian-word-stress
- Wikisource: https://uk.wikisource.org
