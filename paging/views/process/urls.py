from django.urls import path
from . import *

urlpatterns = [
    path('list/', list_process, name='list_process')
]
