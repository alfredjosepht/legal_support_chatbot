# NLP-Based Legal Support Chatbot for Students (Indian Law)

## 📌 Overview

Students often face issues such as **harassment, discrimination, ragging, cyber abuse, threats, or physical violence**, but lack clarity about:

- Which **Indian laws** apply  
- Whether **special laws like POCSO** are involved  
- What **initial procedural steps** (e.g., FIR filing) are generally followed  

This project implements an **NLP-based legal support chatbot** that:

- Understands student problems written in **natural or broken English**
- Identifies the **probable category of offence**
- Maps the issue to **relevant Indian laws and sections**
- Provides **primary procedural guidance**
- Includes a **secure login system**
- Offers a **web-based interface using Streamlit**

> ⚠️ **Disclaimer**  
> This system provides **legal information and procedural guidance only**.  
> It does **not** provide legal advice, legal opinions, or determine guilt or outcomes.

---

## ✨ Features

- Natural Language Processing using **spaCy**
- Machine Learning–based issue classification
- Rule-based legal reasoning (POCSO, discrimination, etc.)
- Indian law mapping:
  - Indian Penal Code (IPC)
  - POCSO Act
  - Information Technology Act
  - SC/ST (Prevention of Atrocities) Act
  - UGC Regulations
- Automatic **POCSO detection** based on age
- Secure **login & registration system**
- Web interface built with **Streamlit**
- Modular and extensible architecture

---

## 🏗️ Project Structure

```text
legal_support_chatbot/
│
├── app/
│   ├── main.py                  # CLI entry point
│   ├── cli.py                   # Command-line interface
│   └── web.py                   # Streamlit web frontend
│
├── nlp/
│   ├── preprocessing.py         # Text cleaning (spaCy)
│   ├── entity_extractor.py      # Age, caste, medium extraction
│   ├── classifier.py            # ML-based issue classification
│   ├── train_classifier.py      # Model training script
│   ├── domain_model.pkl         # Trained ML model
│   └── vectorizer.pkl           # TF-IDF vectorizer
│
├── rules/
│   ├── rule_engine.py           # Central legal reasoning engine
│   ├── age_rules.py             # Minor/POCSO rules
│   ├── discrimination_rules.py  # Caste/race discrimination rules
│   └── institutional_rules.py   # College/institutional misconduct
│
├── knowledge_base/
│   └── law_mapping.json         # Indian law & section mapping
│
├── response/
│   └── generator.py             # Final response generation
│
├── utils/
│   ├── auth_db.py               # Login & authentication (SQLite)
│   ├── law_loader.py            # Loads law mappings
│   └── helpers.py               # Utility helpers
│
├── data/
│   └── training/
│       └── domain_dataset.csv   # Training dataset
│
├── requirements.txt             # Python dependencies
├── README.md                    # Project documentation
└── .gitignore                   # Git ignore rules
```

## 🧰 Technology Stack

- **Python 3.10+**
- **spaCy** – Natural Language Processing
- **scikit-learn** – Machine Learning
- **Streamlit** – Web Interface
- **SQLite** – Authentication Database
- **Git & GitHub**


## ⚙️ Installation & Setup (Linux / Fedora)

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/<your-username>/legal_support_chatbot.git
cd legal_support_chatbot
```
### 2️⃣ Create and Activate Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```
### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
Install spaCy language model:
```
```bash
python -m spacy download en_core_web_sm
```
## 🧠 Train the ML Model (First Time Only)

```bash
python -m nlp.train_classifier
```
This generates:

- `nlp/domain_model.pkl`
- `nlp/vectorizer.pkl`

---

## ▶️ Running the Application

### 🌐 Web Interface (Recommended)

```bash
streamlit run app/web.py
```
Open in browser:

```text
http://localhost:8501
```
### 🖥️ Command Line Interface (Optional)

```bash
python -m app.main
```
## 🔐 Login System

- Users must **register before login**
- Credentials are stored in **SQLite**
- Passwords are **securely hashed**
- Chatbot access is allowed **only after authentication**

Database file:

```text
data/users.db
```
> This file is excluded from GitHub using `.gitignore`.

---

## 🧪 Sample Inputs

```text
my friends teased me about my caste
my senior punched me
i am 16 and teacher touched me
someone created fake account using my photo
college is holding my certificates
