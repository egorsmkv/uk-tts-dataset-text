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
python tools/extract_exclamations.py --in_file data/raw/boh_joho_batkiv.txt >> data/exclamations.txt
python tools/extract_exclamations.py --in_file data/raw/boyci_za_pravdu.txt >> data/exclamations.txt
python tools/extract_exclamations.py --in_file data/raw/chorna_rada.txt >> data/exclamations.txt
python tools/extract_exclamations.py --in_file data/raw/duma_mushketery.txt >> data/exclamations.txt
python tools/extract_exclamations.py --in_file data/raw/franko.txt >> data/exclamations.txt
python tools/extract_exclamations.py --in_file data/raw/leontovich_hronika_grechok.txt >> data/exclamations.txt

python tools/extract_questions.py --in_file data/raw/boh_joho_batkiv.txt >> data/questions.txt
python tools/extract_questions.py --in_file data/raw/boyci_za_pravdu.txt >> data/questions.txt
python tools/extract_questions.py --in_file data/raw/chorna_rada.txt >> data/questions.txt
python tools/extract_questions.py --in_file data/raw/duma_mushketery.txt >> data/questions.txt
python tools/extract_questions.py --in_file data/raw/franko.txt >> data/questions.txt
python tools/extract_questions.py --in_file data/raw/leontovich_hronika_grechok.txt >> data/questions.txt

python tools/extract_obvious.py --in_file data/raw/boh_joho_batkiv.txt >> data/obvious.txt
python tools/extract_obvious.py --in_file data/raw/boyci_za_pravdu.txt >> data/obvious.txt
python tools/extract_obvious.py --in_file data/raw/chorna_rada.txt >> data/obvious.txt
python tools/extract_obvious.py --in_file data/raw/duma_mushketery.txt >> data/obvious.txt
python tools/extract_obvious.py --in_file data/raw/franko.txt >> data/obvious.txt
python tools/extract_obvious.py --in_file data/raw/leontovich_hronika_grechok.txt >> data/obvious.txt
```

### Add stresses

```bash
python tools/add_stresses.py --in_file datasets/unstressed.txt >> datasets/stressed.txt
```

## Acknowledgements

- Ukrainian word stress: https://github.com/lang-uk/ukrainian-word-stress
- Wikisource: https://uk.wikisource.org
