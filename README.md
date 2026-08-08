# 🐦 NLP with Disaster Tweets

An End-to-End Natural Language Processing and Machine Learning Classification Project using the **NLP with Disaster Tweets** dataset from Kaggle.

---

# 📑 Table of Contents

* [📖 Project Overview](#-project-overview)
* [✨ Project Highlights](#-project-highlights)
* [🏗️ Project Architecture](#️-project-architecture)
* [🔄 Machine Learning Workflow](#-machine-learning-workflow)
* [⭐ Features](#-features)
* [💻 Technology Stack](#-technology-stack)
* [📂 Repository Structure](#-repository-structure)
* [📊 Dataset](#-dataset)
* [🔍 Exploratory Data Analysis](#-exploratory-data-analysis)
* [🧹 Data Preprocessing](#-data-preprocessing)
* [⚙️ Feature Engineering](#️-feature-engineering)
* [🤖 Machine Learning Models](#-machine-learning-models)
* [📈 Model Evaluation](#-model-evaluation)
* [🏆 Results](#-results)
* [📚 Documentation](#-documentation)
* [🚀 Installation & Usage](#-installation--usage)
* [📦 Project Outputs](#-project-outputs)
* [📊 Repository Statistics](#-repository-statistics)
* [🎯 Learning Outcomes](#-learning-outcomes)
* [🔮 Future Improvements](#-future-improvements)
* [🌐 Connect with Me](#-connect-with-me)
* [👩‍💻 About the Author](#-about-the-author)
* [🤝 Contributing](#-contributing)
* [🙏 Acknowledgements](#-acknowledgements)
* [📜 License](#-license)
* [⭐ Support the Project](#-support-the-project)

---

# 📖 Project Overview

The **NLP with Disaster Tweets** project is an end-to-end Natural Language Processing and Machine Learning solution developed using the **NLP with Disaster Tweets** dataset from Kaggle.

The objective is to build a predictive model capable of determining whether a tweet refers to a **real disaster** or is simply using disaster-related terminology in a non-disaster context.

This is a binary text classification problem where:

* `0` represents a tweet that does **not** describe a real disaster.
* `1` represents a tweet that **does** describe a real disaster.

Unlike conventional tabular classification problems, this project works primarily with unstructured textual data. Tweets can contain URLs, user mentions, hashtags, punctuation, numbers, informal language, and context-dependent words.

Therefore, the project focuses on transforming raw text into meaningful numerical representations before applying machine learning algorithms.

The complete project follows a structured workflow including:

* Data Collection
* Data Understanding
* Exploratory Data Analysis
* Text Cleaning
* Data Preprocessing
* Feature Extraction
* Machine Learning Model Training
* Model Comparison
* Model Evaluation
* Final Model Selection
* Prediction Generation
* Kaggle Submission

---

# ✨ Project Highlights

✔ Complete End-to-End Natural Language Processing Pipeline

✔ Exploratory Data Analysis (EDA)

✔ Text Cleaning & Preprocessing

✔ Missing Value Analysis

✔ TF-IDF Feature Extraction

✔ Unigram & Bigram Features

✔ Multiple Machine Learning Algorithms

✔ Model Comparison & Evaluation

✔ Classification Report

✔ Confusion Matrix

✔ Kaggle Submission Generation

✔ Reusable Preprocessing Module

✔ Modular Repository Structure

✔ Reproducible Jupyter Notebook Workflow

✔ Comprehensive Project Documentation

✔ GitHub Portfolio Ready

---

# 🏗️ Project Architecture

The project follows a lightweight modular architecture designed specifically for an individual Machine Learning and NLP project.

Each component has a dedicated responsibility:

* **data/** – Local location for the Kaggle training and testing datasets.
* **notebooks/** – Jupyter Notebook containing the complete project workflow.
* **src/** – Reusable Python source code used by the project.
* **requirements.txt** – Python dependencies required to reproduce the project.
* **README.md** – Complete project documentation.
* **CITATION.cff** – Citation metadata for the repository.
* **LICENSE** – MIT License information.
* **.gitignore** – Prevents datasets, generated files, environments, and unnecessary files from being committed.

The repository intentionally avoids unnecessary folders and documentation files while retaining the components required for a clean and reproducible project.

---

# 🔄 Machine Learning Workflow

This project follows a complete Natural Language Processing and Machine Learning lifecycle consisting of the following stages:

1. Data Collection
2. Data Understanding
3. Exploratory Data Analysis
4. Text Cleaning
5. Data Preprocessing
6. Train-Validation Split
7. TF-IDF Feature Extraction
8. Model Building
9. Model Comparison
10. Model Evaluation
11. Best Model Selection
12. Final Model Training
13. Test Prediction
14. Kaggle Submission Generation

The workflow can be summarized as:

```text
Raw Tweets
     ↓
Data Understanding
     ↓
Exploratory Data Analysis
     ↓
Text Cleaning & Preprocessing
     ↓
Train / Validation Split
     ↓
TF-IDF Vectorization
     ↓
Machine Learning Models
     ↓
Model Comparison
     ↓
Model Evaluation
     ↓
Best Model Selection
     ↓
Final Model Training
     ↓
Test Prediction
     ↓
submission.csv
```

Following a structured workflow ensures reproducibility, organized experimentation, and a clear separation between data preparation, feature extraction, model development, and evaluation.

---

# ⭐ Features

## 📊 Data Analysis

* Comprehensive Dataset Exploration
* Dataset Shape and Structure Analysis
* Missing Value Analysis
* Target Class Distribution
* Tweet Length Analysis
* Keyword Frequency Analysis
* Sample Tweet Inspection
* Statistical Summary

---

## 🧹 Data Preprocessing

* Lowercase Conversion
* URL Removal
* User Mention Removal
* Hashtag Symbol Removal
* Number Removal
* Punctuation Removal
* Whitespace Normalization
* Missing Value Handling
* Clean Text Generation

---

## 📈 Data Visualization

* Target Distribution
* Tweet Length Distribution
* Tweet Length Comparison by Target
* Keyword Frequency Visualization
* Missing Value Analysis
* Model Performance Comparison
* Confusion Matrix

---

## 🤖 Natural Language Processing

* Text Cleaning
* Stop Word Removal
* TF-IDF Vectorization
* Unigram Features
* Bigram Features
* Sparse Text Feature Representation

---

## 🧠 Machine Learning

* Multinomial Naive Bayes
* Logistic Regression
* Linear Support Vector Machine
* Model Comparison
* Performance Evaluation
* Final Model Selection

---

## 📦 Outputs

* Cleaned Text Data
* TF-IDF Feature Matrix
* Model Evaluation Metrics
* Confusion Matrix
* Test Predictions
* Kaggle Submission File

---

# 💻 Technology Stack

| Category                    | Technologies                      |
| --------------------------- | --------------------------------- |
| Programming Language        | Python                            |
| Development Environment     | Jupyter Notebook                  |
| Data Analysis               | Pandas, NumPy                     |
| Data Visualization          | Matplotlib, Seaborn               |
| Natural Language Processing | Scikit-learn, Regular Expressions |
| Feature Extraction          | TF-IDF                            |
| Machine Learning            | Scikit-learn                      |
| Version Control             | Git, GitHub                       |
| Dataset Source              | Kaggle NLP with Disaster Tweets   |

---

# 📂 Repository Structure

```text
NLP-Disaster-Tweets/
│
├── data/
│   ├── train.csv
│   └── test.csv
│
├── notebooks/
│   └── NLP_Disaster_Tweets.ipynb
│
├── src/
│   └── preprocessing.py
│
├── .gitignore
├── CITATION.cff
├── LICENSE
├── README.md
└── requirements.txt
```

### Directory Description

| File / Directory       | Purpose                                                       |
| ---------------------- | ------------------------------------------------------------- |
| `data/`                | Local location for the Kaggle dataset                         |
| `notebooks/`           | Complete NLP and Machine Learning workflow                    |
| `src/`                 | Reusable project source code                                  |
| `src/preprocessing.py` | Text preprocessing functionality                              |
| `.gitignore`           | Prevents unnecessary and generated files from being committed |
| `CITATION.cff`         | Citation metadata                                             |
| `LICENSE`              | MIT License                                                   |
| `README.md`            | Complete project documentation                                |
| `requirements.txt`     | Python dependencies                                           |

> The dataset files are shown in the structure above to illustrate the expected local setup. They are not intended to be committed to GitHub.

---

# 📊 Dataset

## Dataset Source

The project uses the **NLP with Disaster Tweets** dataset provided by Kaggle.

### Competition

[NLP with Disaster Tweets](https://www.kaggle.com/competitions/nlp-getting-started)

The competition focuses on identifying whether tweets describe actual disasters.

The dataset contains real tweets that have been labeled for supervised binary classification.

---

## Files Used

| File        | Description                                              |
| ----------- | -------------------------------------------------------- |
| `train.csv` | Training dataset containing tweet text and target labels |
| `test.csv`  | Testing dataset without target labels                    |

---

## Dataset Features

| Feature    | Description                                            |
| ---------- | ------------------------------------------------------ |
| `id`       | Unique identifier for each tweet                       |
| `keyword`  | Disaster-related keyword extracted from the tweet      |
| `location` | Location associated with the tweet                     |
| `text`     | Original tweet text                                    |
| `target`   | Target variable available only in the training dataset |

---

## Target Variable

| Value | Meaning             |
| ----: | ------------------- |
|   `0` | Not a real disaster |
|   `1` | Real disaster       |

The training dataset contains **7,613 labeled tweets**.

---

# 🔍 Exploratory Data Analysis

Exploratory Data Analysis was performed to understand the structure, distribution, and characteristics of the tweet dataset before building the classification models.

The analysis focused on:

* Dataset structure
* Missing values
* Target distribution
* Tweet length
* Keyword frequency
* Text characteristics
* Differences between the two target classes

---

## 📊 Target Distribution

The distribution of the target variable was examined to understand the representation of real disaster and non-disaster tweets.

This analysis helps determine whether there is significant class imbalance that could influence model training and evaluation.

---

## 📉 Missing Value Analysis

Missing values were investigated across the dataset.

The `keyword` and `location` columns contain missing observations. The `text` column provides the primary input used for the NLP pipeline, while `target` provides the supervised learning label in the training data.

---

## 📏 Tweet Length Analysis

Tweet length was calculated to understand the distribution of textual content.

The analysis also compared tweet lengths between the two target classes to investigate whether real disaster tweets and non-disaster tweets show noticeable differences.

---

## 🔤 Keyword Analysis

The frequency of disaster-related keywords was examined to identify commonly occurring terms.

Keyword analysis provides additional insight into the vocabulary present within the dataset and the types of disaster-related concepts represented in the tweets.

---

## 📝 Sample Tweet Analysis

Examples from both target classes were inspected to understand the contextual nature of the classification problem.

This is particularly important because a disaster-related word does not necessarily indicate that the tweet is describing an actual disaster.

---

# 🧹 Data Preprocessing

Text preprocessing is one of the most important stages of this project because raw social media text contains considerable noise.

The preprocessing pipeline transforms the original tweets into cleaner and more consistent text before feature extraction.

---

## Lowercase Conversion

All text is converted to lowercase.

For example:

```text
Earthquake
EARTHQUAKE
earthquake
```

are normalized to:

```text
earthquake
```

This prevents different capitalizations of the same word from being treated as separate features.

---

## URL Removal

URLs are removed from the tweets because the actual web addresses generally do not provide useful information for this classification task.

---

## User Mention Removal

Twitter mentions such as:

```text
@username
```

are removed to reduce noise caused by individual usernames.

---

## Hashtag Processing

The hashtag symbol is removed while preserving the word itself.

For example:

```text
#earthquake
```

becomes:

```text
earthquake
```

This allows the semantic information contained in the hashtag to remain available to the model.

---

## Number Removal

Numerical characters are removed to reduce unnecessary variation in the textual representation.

---

## Punctuation Removal

Punctuation marks are removed to reduce textual noise and create a more standardized representation.

---

## Whitespace Normalization

Extra spaces and unnecessary whitespace are removed.

This produces a cleaner text representation before feature extraction.

---

## Stop Word Removal

Common English stop words are removed during TF-IDF vectorization.

This reduces the influence of extremely common words that generally contribute less discriminative information to the classification task.

---

## Preprocessing Pipeline

```text
Raw Tweet
    ↓
Lowercase Conversion
    ↓
URL Removal
    ↓
User Mention Removal
    ↓
Hashtag Symbol Removal
    ↓
Number Removal
    ↓
Punctuation Removal
    ↓
Whitespace Normalization
    ↓
Stop Word Removal
    ↓
Clean Text
```

---

# ⚙️ Feature Engineering

Since machine learning algorithms require numerical input, the cleaned tweet text must be transformed into a numerical representation.

## TF-IDF Vectorization

**TF-IDF (Term Frequency-Inverse Document Frequency)** was used to convert the cleaned tweets into numerical feature vectors.

TF-IDF assigns greater importance to words that are useful for distinguishing documents while reducing the influence of words that occur frequently throughout the entire dataset.

---

## Term Frequency

Term Frequency measures how frequently a particular term appears within a document.

A word that appears multiple times in a tweet receives a higher term-frequency contribution.

---

## Inverse Document Frequency

Inverse Document Frequency reduces the importance of words that occur across many documents and increases the relative importance of more distinctive terms.

---

## N-Gram Features

The TF-IDF vectorizer uses both **unigrams and bigrams**.

### Unigrams

Individual words are treated as features.

Example:

```text
major
earthquake
reported
```

### Bigrams

Pairs of consecutive words are treated as features.

Example:

```text
major earthquake
earthquake reported
```

Using both unigrams and bigrams allows the model to capture individual terms as well as short phrases.

---

## TF-IDF Configuration

The vectorizer was configured using:

```python
TfidfVectorizer(
    stop_words="english",
    max_features=10000,
    ngram_range=(1, 2)
)
```

The vectorizer is fitted on the training text and subsequently used to transform validation and test data.

This prevents information from the validation and test datasets from influencing the learned feature vocabulary.

---

# 🤖 Machine Learning Models

Several supervised classification algorithms were implemented and compared.

The following models were trained:

* Multinomial Naive Bayes
* Logistic Regression
* Linear Support Vector Machine

Each model was trained using the same TF-IDF feature representation to ensure a fair comparison.

---

## Multinomial Naive Bayes

Multinomial Naive Bayes is a probabilistic classification algorithm that is widely used for text classification.

It works particularly well with high-dimensional sparse representations such as TF-IDF.

### Importance

* Efficient for text classification
* Computationally inexpensive
* Works well with sparse feature matrices
* Provides a strong baseline for NLP problems

---

## Logistic Regression

Logistic Regression is a supervised classification algorithm used to estimate the probability of an observation belonging to a particular class.

It provides a strong linear baseline for binary text classification.

### Importance

* Effective for binary classification
* Performs well with high-dimensional sparse data
* Computationally efficient
* Easy to compare and interpret

---

## Linear Support Vector Machine

Linear Support Vector Machine attempts to identify an effective decision boundary between the two target classes.

It is particularly suitable for text classification because TF-IDF produces a high-dimensional sparse feature representation.

### Importance

* Effective for high-dimensional data
* Performs well with sparse text features
* Commonly used for NLP classification
* Efficient for large feature spaces

---

## Model Comparison

All three models were evaluated using the same validation dataset and TF-IDF representation.

The validation performance was compared to identify the strongest candidate model for the final prediction stage.

---

# 📈 Model Evaluation

The training dataset was divided into training and validation subsets using an **80:20 split**.

The validation set was kept separate from the model training process and was used to compare the candidate classifiers.

---

## Evaluation Metrics

The following metrics were considered:

### Accuracy

Measures the proportion of correctly classified observations among all observations.

### Precision

Measures how many observations predicted as a particular class actually belong to that class.

### Recall

Measures how many of the actual observations belonging to a class were correctly identified.

### F1-Score

The harmonic mean of precision and recall.

F1-score provides a balanced measure when both false positives and false negatives are important.

### Classification Report

The classification report provides precision, recall, F1-score, and support for each target class.

### Confusion Matrix

The confusion matrix provides a detailed breakdown of:

* True Positives
* True Negatives
* False Positives
* False Negatives

This makes it easier to understand the types of classification errors made by the selected model.

---

# 🏆 Results

After training and comparing the candidate machine learning algorithms, the best-performing model was selected based on validation performance.

The selected model was then retrained using the complete labeled training dataset.

The final model was used to generate predictions for the unseen Kaggle test dataset.

---

## Kaggle Result

The final submission was evaluated on the Kaggle public leaderboard.

### Public Leaderboard Score

**0.77627**

This result serves as the current benchmark for the implemented traditional NLP and Machine Learning pipeline.

---

## Final Submission

The predictions were stored in the required Kaggle format:

```text
id,target
```

The resulting file is:

```text
submission.csv
```

The submission file is treated as a reproducible project output and is not required to be stored in the GitHub repository.

---

# 📚 Documentation

The main documentation for this project is maintained directly in this `README.md`.

The Jupyter Notebook contains the complete executable workflow, including:

* Data loading
* Dataset inspection
* Exploratory Data Analysis
* Text preprocessing
* TF-IDF feature extraction
* Model training
* Model comparison
* Evaluation
* Prediction generation
* Submission creation

This approach keeps the repository lightweight while ensuring that the complete methodology remains documented and reproducible.

---

# 🚀 Installation & Usage

## Clone the Repository

```bash
git clone https://github.com/itsnatashasingh/NLP-Disaster-Tweets.git
```

Navigate to the project directory:

```bash
cd NLP-Disaster-Tweets
```

---

## Create a Virtual Environment

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Download the Dataset

Download the competition dataset from Kaggle:

[NLP with Disaster Tweets — Dataset](https://www.kaggle.com/competitions/nlp-getting-started/data)

Place the downloaded files inside the `data/` directory:

```text
data/
├── train.csv
└── test.csv
```

---

## Launch Jupyter Notebook

```bash
jupyter notebook
```

Open:

```text
notebooks/NLP_Disaster_Tweets.ipynb
```

Run the notebook sequentially from beginning to end to reproduce the complete workflow.

---

# 📦 Project Outputs

Running the notebook generates the following outputs:

* 📊 Exploratory Data Analysis visualizations
* 🧹 Cleaned tweet text
* 🔢 TF-IDF feature representation
* 🤖 Trained machine learning models
* 📈 Model evaluation metrics
* 📋 Classification report
* 📉 Confusion matrix
* 📄 Kaggle submission file

The final competition submission is generated as:

```text
submission.csv
```

---

# 📊 Repository Statistics

| Category                         |                                     Count |
| -------------------------------- | ----------------------------------------: |
| Programming Language             |                                         1 |
| Dataset                          |                                         1 |
| NLP Feature Extraction Technique |                                         1 |
| Text Classification Models       |                                         3 |
| Major NLP Preprocessing Stages   |                                        8+ |
| Evaluation Metrics               |                                         6 |
| Jupyter Notebooks                |                                         1 |
| Reusable Source Modules          |                                         1 |
| Repository Type                  | End-to-End NLP & Machine Learning Project |

---

# 🎯 Learning Outcomes

This project demonstrates practical knowledge of:

* Python Programming
* Data Collection
* Data Cleaning
* Data Preprocessing
* Exploratory Data Analysis
* Data Visualization
* Natural Language Processing
* Text Classification
* Regular Expressions
* Stop Word Removal
* N-Grams
* TF-IDF Feature Extraction
* Supervised Machine Learning
* Binary Classification
* Model Comparison
* Model Evaluation
* Classification Metrics
* Git & GitHub
* Kaggle Competition Workflow
* Reproducible Machine Learning Workflows
* Project Documentation

The project also demonstrates how a traditional Machine Learning workflow can be adapted to unstructured textual data.

---

# 🔮 Future Improvements

Possible enhancements for this project include:

* Advanced text normalization
* Stemming
* Lemmatization
* Character-level n-grams
* Word embeddings
* Word2Vec
* GloVe
* FastText
* Incorporating `keyword` and `location` features
* Hyperparameter Optimization
* K-Fold Cross Validation
* Ensemble Learning
* XGBoost
* LightGBM
* CatBoost
* LSTM-based text classification
* GRU-based text classification
* BERT and other Transformer-based models
* Model Explainability
* Streamlit Web Application Deployment
* Automated Model Training
* Experiment Tracking

These improvements could potentially increase classification performance beyond the current traditional NLP baseline.

---

# 🌐 Connect with Me

---

# 👩‍💻 About the Author

## Natasha Singh

I'm an undergraduate student pursuing **B.Sc. Information Technology (Artificial Intelligence)** with a strong interest in Data Science, Machine Learning, Artificial Intelligence, and Software Development.

I enjoy working with real-world datasets, participating in Kaggle competitions, and building practical projects that demonstrate complete and reproducible Machine Learning workflows.

This repository reflects my approach to solving a Natural Language Processing classification problem through a structured workflow—from raw text preprocessing and feature extraction to model comparison, evaluation, and prediction.

If you enjoyed exploring this project, feel free to connect with me or check out my other work.

**LinkedIn** - [Natasha Singh](https://www.linkedin.com/in/natasha-singh-it28)

**Kaggle** - [natashasingh20](https://www.kaggle.com/natashasingh20)

**GitHub** - [itsnatashasingh](https://github.com/itsnatashasingh)

**Website** - [natasha-singh.lovable.app](https://natasha-singh.lovable.app)

---

# 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

If you'd like to contribute:

1. Fork this repository.
2. Create a new feature branch.
3. Commit your changes.
4. Push your branch.
5. Open a Pull Request.

For major changes, please open an issue first to discuss what you would like to change.

---

# 🙏 Acknowledgements

Special thanks to:

* **Kaggle** for providing the NLP with Disaster Tweets dataset and competition platform.
* **The open-source Python community** for developing the libraries used throughout this project.
* **Pandas** for data manipulation and analysis.
* **NumPy** for numerical computation.
* **Matplotlib and Seaborn** for data visualization.
* **Scikit-learn** for TF-IDF feature extraction, machine learning algorithms, and model evaluation tools.

---

# 📜 License

This project is licensed under the **MIT License**.

See the [LICENSE](LICENSE) file for more information.

---

# ⭐ Support the Project

If you found this project useful or interesting:

* ⭐ Star the repository
* 🍴 Fork the repository
* 🐛 Report issues
* 💡 Suggest improvements
* 🔗 Share the project

Your feedback and support are appreciated.
