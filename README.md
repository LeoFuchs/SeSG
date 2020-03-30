# SeSG (Search String Generator)

Implementation and experimentation of SeSG, a search string generator that uses text mining techniques to build a search string from a supplied Quasi-Gold Standard.

### :warning: Note

This is a research algorithm, susceptible to errors and imperfections.

### :file_folder: Structure
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

###  :runner: Running

To run SeSG, simply run some of the .py files present at the root of the directory.

####  :one: Azeem et al.

The file `SeSG-azeem-random.py` performs the experiment for the study by Azeem et al. [[1]](#1). For this to happen, some parameters passed within the code must be:

```bash
    author = 'azeem'
    pub_year_one = 2018  # 0 = disable pub_year
    pub_year_two = 1999  # 0 = disable pub_year
    qgs_size = 5
    gs_size = 15
```

####  :two: Hosseini et al.

####  :three: Vasconcellos et al.

###  :bar_chart: Results

###   :bangbang: Requirements
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

### :page_facing_up: References
<a id="1">[1]</a> 
Dijkstra, E. W. (1968). 
Go to statement considered harmful. 
Communications of the ACM, 11(3), 147-148.
