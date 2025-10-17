from django.db import connection

def create_tables():    
    with connection.cursor() as cursor:
        pass
        # tables 
