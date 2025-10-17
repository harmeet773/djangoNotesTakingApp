from django.apps import AppConfig
from .db_setup import create_tables


class NotestakingappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'notesTakingApp'
    
    def ready(self):
        # code in the ready functions/hook runs when the app is loaded 
        create_tables()