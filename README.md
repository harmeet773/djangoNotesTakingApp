# Django Notes Taking App

A simple **Notes Taking Web Application** built with **Django** where users can create and view their notes.

---

## Features

1. **User Authentication**
   - Users can register by providing username, email, and password.
   - Users can login and logout.
   
2. **Notes Management**
   - One user can have multiple notes (one-to-many relationship).
   - Notes store **title, content, creation timestamp**.
   - New notes appear on top.

3. **Database**
   - Uses **SQLite** as the database.
   - This project does not use Django models.
   - Tables (`users` and `notes`) are created via **raw SQL commands** rather than the ORM.
   - Sessions are handled using Django’s default session framework.

---
## Project Screenshots

### Home Page
![Home page](.\assests\homepage.png)

### Login
![Login](.\assests\login.png)

### Notes
![Notes 1](.\assests\notes1.png)
![Notes 2](.\assests\notes2.png)

### Register
![Register](.\assests\register.png)

## Installation & Setup

This project was created with python version 3.12.8 
### 1. Clone the repository
### 2. Create a virtual environment (optional but recommended)
```bash
python -m venv venv
```
### 3. Activate the virtual environment
Windows:
```bash
venv\Scripts\activate
```
macOS/Linux:
```bash
source venv/bin/activate
```
### 4. Install dependencies
```bash
pip install -r requirements.txt
```
### 5. Apply migrations
```bash
python manage.py migrate
```
### 6. Run the development server
```bash
Run the development server
```

### 7. Open in Browser
Go to: http://127.0.0.1:8000/ to access the app.

