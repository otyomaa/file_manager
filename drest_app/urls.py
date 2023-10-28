from django.urls import path
from .views import *

urlpatterns = [
    path('upload/', upload_file, name='upload_file'),
    path('files/', list_files, name='list_files'),
]
