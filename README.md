# 🧠 Django Online Exam Portal

A simple and secure Online Examination System built using **Django**.  
This application allows users to register, log in, attempt multiple programming language exams, and get instant results.

---

## 📌 Overview

The Django Online Exam Portal is a web-based MCQ examination system where users can:

- Create an account (Signup)
- Login securely
- Attempt different subject exams
- Submit answers
- View instant results with performance feedback

This project demonstrates Django authentication, form handling, score evaluation logic, and template rendering.

---

## 🚀 Features

- ✅ User Registration System
- ✅ Secure Login & Logout
- ✅ Java Exam
- ✅ Python Exam
- ✅ C++ Exam
- ✅ Automatic Score Calculation
- ✅ Result Page with Performance Feedback
- ✅ Responsive UI using Bootstrap
- ✅ CSRF Protection

---

## 🧩 Concepts Used

### 🔹 Django Concepts
- Function Based Views (FBV)
- Django ModelForm
- Django Authentication System
- `login_required` decorator
- Template Inheritance
- CSRF Token Protection
- POST Request Handling
- HttpResponseRedirect
- Password Encryption using `set_password()`

---

## 📂 Project Structure

```
authenticationproject/
│
├── authenticationproject/        # Main project folder
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py (if available)
│
├── testapp/                      # Django app
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   ├── migrations/
│   │   └── __init__.py
│   └── __pycache__/
│
├── templates/
│   ├── registration/
│   │   └── login.html
│   │
│   └── testapp/
│       ├── base.html
│       ├── home.html
│       ├── cpp.html
│       ├── javaexam.html
│       ├── python.html
│       ├── result.html
│       ├── logout.html
│       └── signup.html
│
├── db.sqlite3
├── manage.py
├── requirements.txt
└── .gitignore
```

## ⚙️ How to Run

- Clone the Repository ```git clone https://github.com/rajatkumarbal779/django-online-exam-portal.git```
- Install Required Dependencies ```pip install -r requirements.txt ```
- Apply Database Migrations ```python manage.py migrate```
- (Optional) Create Superuser ```python manage.py createsuperuser```
- Run the Development Server ```python manage.py runserver```
- Open in Browser ```http://127.0.0.1:8000/```

---

## Author & Contact
<strong>Rajat Kumar Bal</strong><br>
📧 Email: rajatkumarbal961@gmail.com<br>
🔗 <a href="https://www.linkedin.com/in/rajat-kumar-bal">LinkedIn</a>
<div align ="center">
  Made With 💖 by <strong>Rajat</strong>
</div>
