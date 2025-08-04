# 🃏 Doubt Card Game - Django Project

This is a web-based implementation of the classic card game "Doubt" (also known as Cheat or Bluff), built using Django.

## 🚀 Features

- User login and room creation
- Turn-based card play
- "Doubt" action (challenge)
- Victory condition: first player to discard all cards
- Basic web interface (Django templates)

## 🛠️ Tech Stack

- **Backend**: Django 5.2.4
- **Frontend**: Django Templates + HTML/CSS/JavaScript
- **Database**: SQLite (default)
- **Version Control**: Git + GitHub

## 📦 How to Run Locally

1. Clone the repo:
   ```bash
   git clone https://github.com/jeonghyunje/Doubt.git
   cd Doubt
   ```

2. Set up virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install django
   ```

4. Run server:
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

Then open your browser to `http://127.0.0.1:8000/`.


## 📄 License

KNU License © 2025 [jeonghyunje]
