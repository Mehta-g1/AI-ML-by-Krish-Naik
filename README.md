# 🧠 My ML & NLP Bootcamp + MLOps Workspace

> **Private Learning & Reference Repository**

This is my personal, private workspace containing notes, code practices, models, and projects for the Udemy course: **[Complete Machine Learning &amp; NLP Bootcamp MLOps Deployment](https://www.udemy.com/course/complete-machine-learning-nlp-bootcamp-mlops-deployment/)** by **Krish Naik**.

Since I am covering the course materials in a non-linear order based on immediate interest and project needs, the repository structure and progress tracking are updated dynamically as I explore different sections.

---

## 📅 Study Checklist & Progress Tracker

*Feel free to check/uncheck these in any order as they are completed!*

### 🐍 Python & Databases

- [X] **[SQLite3 Database Management](https://github.com/Mehta-g1/AI-ML-by-Krish-Naik/tree/main/14_Working%20with%20sqlite3)**
- [X] **[Logging in Python](https://github.com/Mehta-g1/AI-ML-by-Krish-Naik/tree/main/15_Logging%20in%20Python)**
- [X] **[Concurrency: Multithreading & Multiprocessing](https://github.com/Mehta-g1/AI-ML-by-Krish-Naik/tree/main/16_Python%20multi%20Threading%20and%20Multi%20Processing)**
- [X] **[Python Memory Management & Core Advanced Topics](https://github.com/Mehta-g1/AI-ML-by-Krish-Naik/tree/main/17_Memory%20Management%20with%20Python)**

### 🤖 Machine Learning Algorithms

- [X] **[Linear Regression (End-to-End Project)](https://github.com/Mehta-g1/AI-ML-by-Krish-Naik/tree/main/29_Steps%20By%20Step%20Project%20Implementation%20With%20LifeCycle%20OF%20ML%20Project)**
- [X] **[Feature Engineering & Preprocessing](https://github.com/Mehta-g1/AI-ML-by-Krish-Naik/tree/main/24_feature%20Engineering)**
- [X] **[Decision Tree Classifier & Regressor](https://github.com/Mehta-g1/AI-ML-by-Krish-Naik/tree/main/34_Descision%20Tree%20Classifier%20and%20Regressor)**
- [X] **[Support Vector Machines (SVM) & Regressor (SVR)](https://github.com/Mehta-g1/AI-ML-by-Krish-Naik/tree/main/31_support%20vector%20machines)**

### 🔧 Tools & Version Control

- [X] **[Git & GitHub for Beginners](https://github.com/Mehta-g1/AI-ML-by-Krish-Naik/tree/main/47_Git%20for%20beginners)**

---

## 📁 Repository Structure

```text
├── 14_Working with sqlite3/          # SQLite database interaction, query execution, & assignments
├── 15_Logging in Python/             # Custom loggers, production logging setups, & assignments
├── 16_Python multi Threading and.../ # Concurrency, multithreading, and multiprocessing practices
├── 17_Memory Management with Python/ # Python memory management, garbage collection, and mutability
├── 24_feature Engineering/           # Feature engineering: handling missing values & imbalanced datasets
├── 29_Steps By Step Project.../      # End-to-end regression ML lifecycle (Algerian Forest Fire FWI prediction)
│   ├── models/                       # Trained regression models and scalers (.pkl)
│   └── web app/                      # Flask web application for live user predictions
├── 31_support vector machines/       # Support Vector Classifier (SVC) & Regressor (SVR) implementations
├── 34_Descision Tree Classifier.../  # Decision Tree models, practical implementations, & datasets
├── 47_Git for beginners/             # Git and GitHub basics, cheat sheets, and tutorial notebooks
├── README.md                         # This workspace roadmap & progress tracker
└── requirements.txt                  # Python workspace dependencies
```

---

## 🛠️ Local Environment Setup

To run the notebooks and scripts in this workspace:

1. **Activate virtual environment**:
   ```bash
   # Windows (PowerShell)
   .\venv\Scripts\activate

   # Linux/macOS
   source venv/bin/activate
   ```
2. **Install workspace dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Launch Jupyter Notebook/Lab**:
   ```bash
   jupyter lab
   ```
