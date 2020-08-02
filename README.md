<h1 align="center">
    SeSG (Search String Generator)
</h1> 

<p align="center">
    <img alt="Repository Size" src="https://img.shields.io/github/repo-size/LeoFuchs/SeSG">
    <img alt="Top Language" src="https://img.shields.io/github/languages/top/LeoFuchs/SeSG">
    <img alt="License" src="https://img.shields.io/github/license/LeoFuchs/SeSG">
    <img alt="Stargazers" src="https://img.shields.io/github/stars/LeoFuchs/SeSG?style=social">
</p>

Implementation and experimentation of SeSG, a search string generator that uses text mining techniques to build a search string from a supplied Quasi-Gold Standard.

**Note**: This is a research algorithm, susceptible to errors and imperfections.

### Repository Structure
This is the directory structure. In summary, there is a folder with the results of the experiment (complete-results), a folder with the output of the execution (exits), a folder with the input files of the execution (files-qgs) and the codes that form the SeSG.

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
│   ├── .gitignore
│   ├── LICENSE
│   ├── README.md
│   ├── SeSG.py
│   ├── object-azeem.py
│   ├── object-hosseini.py
│   ├── object-vasconcellos.py
│   └── requirements.txt

```

### SeSG Process

An example of how the SeSG process works is shown in Figure 1. This process begins with the execution of the LDA on a bag-of-words formulated from the selected QGS. Then, BERT is used to find similar terms, used to enrich the search string. Finally, the terms found previously are grouped together and the search string is formulated.

<p align="center"><img align="center" src="https://github.com/LeoFuchs/SeSG/blob/master/images/process.jpg" width="500"></p>

<p align="center"><b> Figure 1. </b>An example of the Topics Extraction and Enrichment and Generation of Search String 
sub-processes of the SeSG process, showing the necessary input parameters and how the search string is developed.</p>

<br>
To executing the SeSG, simply run some of the `.py` files present at the root of the directory.

### Quasi-Experiment Running

There are three `.py` files that perform the experiment SeSG, each with the ideal configuration to perform the experiment in a particular object.

#### 1. Azeem et al.

The file `object-azeem.py` performs the experiment for the study by Azeem et al. [[1]](#1). For this to happen, some parameters passed within the code must be:

```bash
author = 'azeem'
pub_year_one = 2018
pub_year_two = 1999
qgs_size = 5
gs_size = 15
```

#### 2. Hosseini et al.

The file `object-hosseini.py` performs the experiment for the study by Hosseini et al. [[2]](#2). For this to happen, some parameters passed within the code must be:

```bash
author = 'hosseini'
pub_year_one = 2016
pub_year_two = 0
qgs_size = 15
gs_size = 46
```

#### 3. Vasconcellos et al.

The file `object-vasconcellos.py` performs the experiment for the study by Vasconcellos et al. [[3]](#3). For this to happen, some parameters passed within the code must be:

```bash
author = 'vasconcellos'
pub_year_one = 2015
pub_year_two = 0
qgs_size = 10
gs_size = 30
```

### Quasi-Experiment Results

The execution of the `.py` script completely originates in several outputs. The script itself generates the search strings and their respective results as an output on the screen, in addition to a spreadsheet named `author-result.csv` with a compilation of this information presented. 

**Note**: The results found in the `/exits/` folder are exemplifying a random execution of the `SeSG-azeem.py` script.

In addition, in the folder `/exits/snowballing-images/` are the graphs that represent the snowballing of each of the search strings presented, with their nomenclature following the test configuration. For example, `graph-with-0.1-3-7-0.ps` symbolizes that the represented graph has the following configuration: 0.1 min-df, 3 topics, 7 words and 0 similar words.

The output graph represents the connection between the articles present in the GS, showing which of these were found by searching bases (bold nodes), those found through snowballing rounds (filled nodes) and those that were not found after the application of the hybrid approach (dashed nodes).

<p align="center"><img src="https://github.com/LeoFuchs/SeSG/blob/master/images/snowballing-output.png" width="700"></p>

<p align="center"><b> Figure 2. </b>Graph representing the connection between the GS in the Vasconcellos et al. [3] object.</p>


### Requirements
* python 3.6.9
* fuzzywuzzy 0.18.0
* graphviz 0.14
* nltk 3.5
* numpy 1.19.0
* pandas 1.0.5
* pyscopus 0.9.0
* python-Levenshtein 0.12.0
* scikit-learn 0.23.1
* scipy 1.5.1
* torch 1.5.1
* transformers 3.0.2


### References
<a id="1">[1]</a> Azeem, M. I., Palomba, F., Shi, L., & Wang, Q. (2019). [Machine learning techniques for code smell detection: A systematic literature review and meta-analysis.](https://www.sciencedirect.com/science/article/abs/pii/S0950584918302623) Information and Software Technology, 108, 115-138.

<a id="2">[2]</a> Hosseini, S., Turhan, B., & Gunarathna, D. (2017). [A systematic literature review and meta-analysis on cross project defect prediction.](https://ieeexplore.ieee.org/abstract/document/8097045/) IEEE Transactions on Software Engineering, 45(2), 111-147.

<a id="3">[3]</a> Vasconcellos, F. J., Landre, G. B., Cunha, J. A. O., Oliveira, J. L., Ferreira, R. A., & Vincenzi, A. M. (2017). [Approaches to strategic alignment of software process improvement: A systematic literature review.](https://www.sciencedirect.com/science/article/pii/S0164121216301893) Journal of systems and software, 123, 45-63.
