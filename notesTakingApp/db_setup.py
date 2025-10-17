from django.db import connection

def create_tables():    

    with connection.cursor() as cursor:
        # Create users table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY AUTOINCREMENT, 
                username TEXT NOT NULL,
                useremail TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                last_update DATE,
                create_on DATE DEFAULT (DATE('now'))
            )
        ''')

        # Create notes table with foreign key reference to users
        # on ON DELETE CASCADE means Deletes all notes automatically if the user is deleted
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS notes (
                note_id INTEGER PRIMARY KEY AUTOINCREMENT,  
                user_id INTEGER NOT NULL,
                note_title TEXT NOT NULL,
                note_content TEXT NOT NULL,
                last_update DATE,
                created_on DATETIME DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
            )
        ''')

