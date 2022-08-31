# Texts for the Ukrainian Text-to-Speech dataset

## Overview

This repository contains scripts to generate Text-to-Speech datasets (text part of them) for Ukrainian.

## Related works

- https://github.com/egorsmkv/ukrainian-tts-datasets (Open Source Ukrainian Text-to-Speech datasets)

## Install

```bash
pip install --upgrade ukrainian-word-stress

pip install git+https://github.com/NeonBohdan/ukrainian-accentor-transformer.git
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

python tools/add_stresses_only_csv_transformer.py --in_file data/exclamations.txt >> datasets/stressed/exclamations.csv
python tools/add_stresses_only_csv_transformer.py --in_file data/questions.txt >> datasets/stressed/questions.csv
python tools/add_stresses_only_csv_transformer.py --in_file data/obvious.txt >> datasets/stressed/obvious_3.csv
```

### Convert the dataset obtained from the Online Microphone to convenient format

```bash
python tools/prepare_dataset.py --raw_files ../done/lada/ --save_to ../dataset_lada
```

## Acknowledgements

- Ukrainian word stress: https://github.com/lang-uk/ukrainian-word-stress
- Ukrainian accentor: https://github.com/NeonBohdan/ukrainian-accentor-transformer
- Wikisource: https://uk.wikisource.org
