# Formic-LLC-Task
# Django Quiz & Events App

## Goal
Developed a simple Quiz and Events Web Application using Python (Django) and HTML + Tailwind CSS. Users can view quizzes and events, attempt quizzes with dynamic questions, submit answers, and view results.

## Technology Stack
- Backend: Django (latest stable version)
- Database: SQLite
- Frontend: HTML + Tailwind CSS (Django Templates)
- Optional: Django REST Framework

## Models
- **Quiz**: id, title, description, created_at, updated_at  
- **Question**: id, quiz, text, question_type, created_at  
- **Answer**: id, question, text, is_correct  
- **UserSubmission**: id, quiz, user_name, score, submitted_at  
- **UserAnswer**: submission, question, answer, is_correct  
- **Event**: id, title, description, date, location  

## Features
### Quiz Section
- List all available quizzes  
- Start a quiz  
- Dynamically load questions and answers  
- On submission: calculate score, display results, save submission  

### Event Section
- Display upcoming events with title, date, and location  

### Frontend
- Tailwind CSS  
- Pages: Home, Quiz List, Quiz Attempt, Result, Events  

## Bonus (Optional)
- User authentication added  
- Quiz history page added  
- DRF structure prepared  
- Dashboard for adding quizzes/questions (submission error pending)  
- Seed data added via Django admin panel  

## Setup Instructions
1. Clone the repository:  
   ```bash
   git clone https://github.com/yourusername/Formic-LLC-Task.git
   cd "Formic LLC Task"
2. Create virtual environment and activate it:
  python -m venv venv
  source venv/Scripts/activate   # Windows
3. Install dependencies:
   pip install -r requirements.txt
4. Run migrations:
   python manage.py migrate
5. Create superuser (for admin panel):
   python manage.py createsuperuser
6. Run Server:
   python manage.py runserver
7. Access the app at http://127.0.0.1:8000/

============================================================== NOTES =========================================================

Dashboard quiz submission currently has an error after submitting a quiz (pending).

Seed data added manually via admin panel (fixtures not used).   

   
---

✅ **Next step:**  

1. Save this content as `README.md` in your project folder (`Formic LLC Task`).  
2. Open Git Bash in the **same folder**.  
3. Run these commands **to push everything to GitHub**:

```bash
git add .
git commit -m "Add README and initial Django project"
git remote add origin https://github.com/yourusername/Formic-LLC-Task.git
git pull origin main --allow-unrelated-histories
git push -u origin main

NOTE :=================== Replace yourusername with your GitHub username. =========================

   
   

