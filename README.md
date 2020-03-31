# SeSG (Search String Generator)

Implementation and experimentation of SeSG, a search string generator that uses text mining techniques to build a search string from a supplied Quasi-Gold Standard.

### :warning: Note

This is a research algorithm, susceptible to errors and imperfections.

### :file_folder: Repository Structure
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

### :rocket: SeSG Process

<p align="center"><img align="center" src="https://github.com/LeoFuchs/SeSG/blob/master/images/process.jpg" width="500"></p>

  ![Boundary Conditions](https://github.com/LeoFuchs/SeSG/blob/master/images/process.jpg)

To executing the SeSG, simply run some of the `.py` files present at the root of the directory.

###  :runner: Quasi-Experiment Running

There are three `.py` files that perform the SeSG, each with the ideal configuration to perform the experiment with a particular article.

####  :one: Azeem et al.

The file `SeSG-azeem.py` performs the experiment for the study by Azeem et al. [[1]](#1). For this to happen, some parameters passed within the code must be:

```bash
author = 'azeem'
pub_year_one = 2018  # 0 = disable pub_year
pub_year_two = 1999  # 0 = disable pub_year
qgs_size = 5
gs_size = 15
```

####  :two: Hosseini et al.

The file `SeSG-hosseini.py` performs the experiment for the study by Hosseini et al. [[2]](#2). For this to happen, some parameters passed within the code must be:

```bash
author = 'hosseini'
pub_year_one = 2016  # 0 = disable pub_year
pub_year_two = 0  # 0 = disable pub_year
qgs_size = 15
gs_size = 46
```

####  :three: Vasconcellos et al.

The file `SeSG-vasconcellos.py` performs the experiment for the study by Vasconcellos et al. [[3]](#3). For this to happen, some parameters passed within the code must be:

```bash
author = 'vasconcellos'
pub_year_one = 2015  # 0 = disable pub_year
pub_year_two = 0  # 0 = disable pub_year
qgs_size = 10
gs_size = 30
```

###  :bar_chart: Quasi-Experiment Results

The execution of the `.py` script completely originates in several outputs. The script itself generates the search strings and their respective results as an output on the screen, in addition to a spreadsheet named `author-result.csv` with a compilation of this information presented. 

In addition, in the folder `/exits/snowballing-images/` are the graphs that represent the snowballing of each of the search strings presented, with their nomenclature following the test configuration. For example, `graph-with-0.1-3-7-0.ps` symbolizes that the represented graph has the following configuration: 0.1 min-df, 3 topics, 7 words and 0 similar words.

The output graph represents the connection between the articles present in the GS, showing which of these were found by searching bases (red nodes), those found through snowballing rounds (blue nodes) and those that were not found after the application of the hybrid approach (black nodes).

<p align="center"><img src="https://github.com/LeoFuchs/SeSG/blob/master/images/snowballing-output.png" width="500"></p>

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
<a id="1">[1]</a> Azeem, M. I., Palomba, F., Shi, L., & Wang, Q. (2019). [Machine learning techniques for code smell detection: A systematic literature review and meta-analysis.](https://www.sciencedirect.com/science/article/abs/pii/S0950584918302623) Information and Software Technology, 108, 115-138.

<a id="2">[2]</a> Hosseini, S., Turhan, B., & Gunarathna, D. (2017). [A systematic literature review and meta-analysis on cross project defect prediction.](https://ieeexplore.ieee.org/abstract/document/8097045/) IEEE Transactions on Software Engineering, 45(2), 111-147.

<a id="3">[3]</a> Vasconcellos, F. J., Landre, G. B., Cunha, J. A. O., Oliveira, J. L., Ferreira, R. A., & Vincenzi, A. M. (2017). [Approaches to strategic alignment of software process improvement: A systematic literature review.](https://www.sciencedirect.com/science/article/pii/S0164121216301893) Journal of systems and software, 123, 45-63.
