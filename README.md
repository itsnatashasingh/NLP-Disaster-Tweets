# NLP with Disaster Tweets

> A Natural Language Processing and Machine Learning project for classifying tweets as real disaster-related tweets or non-disaster tweets.

[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Jupyter Notebook](https://img.shields.io/badge/Jupyter-Notebook-orange?logo=jupyter&logoColor=white)](https://jupyter.org/)
[![Scikit--learn](https://img.shields.io/badge/Scikit--learn-Machine%20Learning-F7931E?logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Kaggle](https://img.shields.io/badge/Kaggle-Competition-20BEFF?logo=kaggle&logoColor=white)](https://www.kaggle.com/competitions/nlp-getting-started)

---

## Project Links

| Resource | Link |
|---|---|
| **Kaggle Competition** | [NLP with Disaster Tweets](https://www.kaggle.com/competitions/nlp-getting-started) |
| **Kaggle Notebook** | [Tweets NLP](https://www.kaggle.com/code/natashasingh20/tweets-nlp) |
| **GitHub Repository** | [NLP-Disaster-Tweets](https://github.com/itsnatashasingh/NLP-Disaster-Tweets) |

---

## Contact Me

If you have questions, suggestions, or would like to connect regarding this project, feel free to reach out.

- **LinkedIn:** [Natasha Singh](https://www.linkedin.com/in/natasha-singh-it28)
- **GitHub:** [@itsnatashasingh](https://github.com/itsnatashasingh)
- **Kaggle:** [@natashasingh20](https://www.kaggle.com/natashasingh20)
- **Portfolio:** [natasha-singh.lovable.app](https://natasha-singh.lovable.app)

---

## Table of Contents

- [Project Overview](#project-overview)
- [Problem Statement](#problem-statement)
- [Objectives](#objectives)
- [Dataset](#dataset)
- [Project Workflow](#project-workflow)
- [Exploratory Data Analysis](#exploratory-data-analysis)
- [Data Preprocessing](#data-preprocessing)
- [Feature Engineering](#feature-engineering)
- [Machine Learning Models](#machine-learning-models)
- [Model Evaluation](#model-evaluation)
- [Final Model and Prediction](#final-model-and-prediction)
- [Kaggle Result](#kaggle-result)
- [Key Concepts Demonstrated](#key-concepts-demonstrated)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Running the Project](#running-the-project)
- [Technologies Used](#technologies-used)
- [Future Improvements](#future-improvements)
- [Author](#author)
- [License](#license)

---

# Project Overview

Social media platforms generate enormous amounts of textual information during emergencies and natural disasters. However, not every tweet containing disaster-related terminology actually describes a real disaster.

For example, a tweet may contain words such as *fire*, *flood*, or *earthquake* while referring to an unrelated situation.

This project approaches the problem as a **binary text classification task** using Natural Language Processing and Machine Learning.

The objective is to develop a model capable of determining whether a tweet refers to a **real disaster** or is simply using disaster-related language in a non-disaster context.

The project follows a complete machine learning workflow:

```text
Raw Dataset
     ↓
Exploratory Data Analysis
     ↓
Text Preprocessing
     ↓
Train / Validation Split
     ↓
TF-IDF Feature Extraction
     ↓
Machine Learning Models
     ↓
Model Comparison
     ↓
Model Evaluation
     ↓
Final Model Training
     ↓
Test Prediction
     ↓
Kaggle Submission
```

---

# Dataset

The project uses the **NLP with Disaster Tweets** dataset provided through Kaggle.

## Dataset Source

[NLP with Disaster Tweets — Kaggle Competition](https://www.kaggle.com/competitions/nlp-getting-started)

The dataset contains tweets that have been manually labeled according to whether they refer to a real disaster.

---

## Training Dataset

The training dataset contains **7,613 observations** and the following columns:

| Column | Description |
|---|---|
| `id` | Unique identifier for each tweet |
| `keyword` | Disaster-related keyword extracted from the tweet |
| `location` | Location associated with the tweet |
| `text` | Original tweet text |
| `target` | Target classification label |

The target variable contains two classes:

| Value | Meaning |
|---:|---|
| `0` | Not a real disaster |
| `1` | Real disaster |

---

## Test Dataset

The test dataset contains:

| Column | Description |
|---|---|
| `id` | Unique identifier |
| `keyword` | Disaster-related keyword |
| `location` | Location associated with the tweet |
| `text` | Original tweet text |

The `target` column is not included in the test data and must be predicted by the trained model.

---

## Dataset Setup

The raw dataset files are not committed to the repository.

After downloading the dataset from Kaggle, place the files locally as:

```text
data/
├── train.csv
└── test.csv
```

---

# Feature Engineering

Machine learning algorithms require numerical input. Since tweets are textual data, the cleaned text must first be transformed into numerical features.

## TF-IDF Vectorization

**TF-IDF (Term Frequency-Inverse Document Frequency)** was used to convert the cleaned tweets into numerical feature vectors.

TF-IDF assigns greater importance to terms that are useful for distinguishing documents while reducing the influence of terms that occur frequently across the entire corpus.

### Term Frequency

Term Frequency measures how frequently a term appears within an individual document.

### Inverse Document Frequency

Inverse Document Frequency reduces the weight of terms that appear across many documents and increases the relative importance of more distinctive terms.

---

## N-Gram Features

The TF-IDF vectorizer was configured to use both **unigrams and bigrams**.

### Unigrams

Individual words are treated as features.

Example:

```text
major
earthquake
reported
```


