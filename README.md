# SeSG (Search String Generator)

Implementation and experimentation of SeSG, a search string generator that uses text mining techniques to build a search string from a supplied Quasi-Gold Standard.

## Note

This is a search algorithm, susceptible to several errors and imperfections.

## Structure

```bash
├── SeSG
│   ├── complete-results
│   │   ├── review-azeem
│   │   ├── review-hosseini
│   │   └── review-vasconcellos
│   │       ├── doc_lengths.npy
│   ├── exits
│   │   ├── snowballing-images
│   │   ├── manual-exit.csv
│   │   ├── result.csv
│   │   └── sentences.txt
│   ├── qgs-files
│   │   ├── review-azeem
│   │       ├── gs-pdf
│   │       ├── gs-txt
│   │       ├── qgs-txt
│   │       ├── gs.csv
│   │       ├── qgs.csv
│   │   ├── review-hosseini
│   │   └── review-vasconcellos
│   ├── venv
│   ├── SeSG-azeem-random.py
│   ├── SeSG-hosseini-random.py
│   └── SeSG-vasconcellos-random.py

```

## Usage

### Azeem et al.

### Hosseini et al.

### Vasconcellos et al.

## Results

## Requirements
* Python 2.7
* Torch 1.2.0+
* Numpy 1.15.4+
* Pandas 0.23.4+
* Graphviz 0.11+
* scikit-learn 0.20.1+
* Fuzzywuzzy 0.17.0+
* pyscopus 0.9.0
* pytorch_transformers 1.0.0+
* python-Levenshtein 0.12.0
