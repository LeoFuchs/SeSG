# :pushpin: SeSG (Search String Generator)

Implementation and experimentation of SeSG, a search string generator that uses text mining techniques to build a search string from a supplied Quasi-Gold Standard.

## Note

This is a research algorithm, susceptible to errors and imperfections.

## Structure
This is the directory structure. In summary, there is a folder with the results of the quasi-experiment (complete-results), a folder with the output of the execution (exits), a folder with the input files of the execution (files-qgs) and the codes that form the SeSG.

```bash
├── SeSG
│   ├── complete-results
│   │   ├── azeem-review
│   │       └── ...
│   │   ├── hosseini-review
│   │       └── ...
│   │   └── vasconcellos-review
│   │       └── ...
│   ├── exits
│   │   ├── snowballing-images
│   │   ├── manual-exit.csv
│   │   ├── result.csv
│   │   └── sentences.txt
│   ├── files-qgs
│   │   ├── review-azeem
│   │       ├── gs-pdf
│   │       ├── gs-txt
│   │       ├── qgs-txt
│   │       ├── GS.csv
│   │       └── QGS.csv
│   │   ├── review-hosseini
│   │       └── ...
│   │   └── review-vasconcellos
│   │       └── ...
│   ├── README.md
│   ├── SeSG-azeem-random.py
│   ├── requirements.txt
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
