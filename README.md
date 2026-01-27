NLP-Based Legal Support Chatbot for Students (Indian Law)
📌 Overview

Students often face issues such as harassment, discrimination, ragging, cyber abuse, threats, or physical violence, but lack clarity about:

Which Indian laws apply

Whether special laws like POCSO are involved

What initial procedural steps (e.g., FIR filing) are generally followed

This project implements an NLP-based legal support chatbot that:

Understands student problems written in natural or broken English

Identifies the probable category of offence

Maps the issue to relevant Indian laws and sections

Provides primary procedural guidance

Includes a secure login system

Offers a web-based interface using Streamlit

⚠️ Disclaimer
This system provides legal information and procedural guidance only.
It does not provide legal advice, legal opinions, or determine guilt or outcomes.

✨ Features

Natural Language Processing using spaCy

Machine Learning–based issue classification

Rule-based legal reasoning (POCSO, discrimination, etc.)

Indian law mapping:

IPC

POCSO Act

IT Act

SC/ST (Prevention of Atrocities) Act

UGC Regulations

Automatic POCSO detection based on age

Secure login & registration system

Web interface built with Streamlit

Modular and extensible architecture

🏗️ Project Structure
legal_support_chatbot/
│
├── app/
│   ├── main.py              # CLI entry point
│   ├── cli.py               # Command-line interface
│   └── web.py               # Streamlit frontend
│
├── nlp/
│   ├── preprocessing.py
│   ├── entity_extractor.py
│   ├── classifier.py
│   ├── train_classifier.py
│   ├── domain_model.pkl
│   └── vectorizer.pkl
│
├── rules/
│   ├── rule_engine.py
│   ├── age_rules.py
│   ├── discrimination_rules.py
│   └── institutional_rules.py
│
├── knowledge_base/
│   └── law_mapping.json
│
├── response/
│   └── generator.py
│
├── utils/
│   ├── auth_db.py
│   ├── law_loader.py
│   └── helpers.py
│
├── data/
│   └── training/
│       └── domain_dataset.csv
│
├── requirements.txt
├── README.md
└── .gitignore

🧰 Technology Stack

Python 3.10+

spaCy – NLP

scikit-learn – Machine Learning

Streamlit – Web UI

SQLite – Authentication database

Git & GitHub

⚙️ Installation & Setup (Linux / Fedora)
1. Clone the Repository
git clone https://github.com/<your-username>/legal_support_chatbot.git
cd legal_support_chatbot

2. Create and Activate Virtual Environment
python3 -m venv venv
source venv/bin/activate

3. Install Dependencies
pip install -r requirements.txt


Install spaCy language model:

python -m spacy download en_core_web_sm

🧠 Train the ML Model (First Time Only)
python -m nlp.train_classifier


This generates:

nlp/domain_model.pkl

nlp/vectorizer.pkl

▶️ Running the Application
Web Interface (Recommended)
streamlit run app/web.py


Open in browser:

http://localhost:8501

Command Line Interface (Optional)
python -m app.main

🔐 Login System

Users must register before login

Credentials are stored in SQLite

Passwords are securely hashed

Chatbot access is allowed only after authentication

Database file:

data/users.db


This file is excluded from GitHub using .gitignore.

🧪 Sample Inputs
my friends teased me about my caste
my senior punched me
i am 16 and teacher touched me
someone created fake account using my photo
college is holding my certificates

⚖️ Legal Scope Covered

Physical violence

Sexual offences

Child sexual offences (POCSO)

Ragging

Cyber crimes

Caste and racial discrimination

Threats and intimidation

Institutional misconduct

Mental harassment

🛡️ Ethics & Limitations

Does not predict legal outcomes

Does not provide personalized legal advice

Uses neutral and informational language

Final applicability of laws is decided by authorities

Designed as a decision-support system

🚀 Future Enhancements

Location-based police station suggestions

FIR portal integration

Severity scoring

User-specific chat history

PDF report generation

Cloud deployment

🎓 Academic Use

This project is suitable for:

Final-year engineering projects

NLP / AI / ML coursework

Legal informatics demonstrations

Social-impact technology showcases

📜 License

This project is intended for educational and academic use only.

If you want next, I can help you with:

📄 Final project report

🎤 Viva explanation

🖼️ Screenshots & demo guide

☁️ Deployment steps

Just tell me what you need next.
