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
![Home page](djangoNotesTakingApp\assests\homepage.png)

### Login
![Login](djangoNotesTakingApp\assests\login.png)

### Notes
![Notes 1](djangoNotesTakingApp\assests\notes1.png)
![Notes 2](djangoNotesTakingApp\assests\notes2.png)

### Register
![Register](djangoNotesTakingApp\assests\register.png)



