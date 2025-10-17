
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db import connection

from functools import wraps

def login_required(view_func):
    """
    Decorator to ensure the user is logged in.
    Redirects to login page if not.
    """
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.session.get('user_id'):
            return redirect('login')
        return view_func(request, *args, **kwargs)
    return wrapper


def home(request):
    return render(request, 'home.html')  

def register(request):  
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO users (username, useremail, password) VALUES (%s, %s, %s)",
                [username, email, password]
            )
        return redirect('login')
    return render(request, 'register.html')
   
def login_view(request):
    user_id = request.session.get('user_id')
    if user_id:
        return redirect('home')    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']  
        with connection.cursor() as cursor:
            cursor.execute("SELECT user_id FROM users WHERE username=%s AND password=%s", [username, password])
            user = cursor.fetchone()
        if user:
            request.session['user_id'] = user[0]
            return redirect('notes')
        return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

@login_required
def notes(request):
    user_id = request.session.get('user_id')
    if request.method == 'POST':
        note_title = request.POST['note_title']
        note_content = request.POST['note_content']
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO notes (user_id, note_title, note_content) VALUES (%s, %s, %s)", [user_id, note_title, note_content])
    with connection.cursor() as cursor:
        cursor.execute("""    SELECT note_title, note_content ,created_on FROM notes WHERE user_id=%s ORDER BY created_on DESC """, [user_id])
        all_notes = cursor.fetchall()
    return render(request, 'notes.html', {'notes': all_notes})     

@login_required
def logout_view(request):
    # Clear the session
    request.session.flush()
    return redirect('home') 

