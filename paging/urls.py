from django.urls import path, include
from .views import *

app_name = 'paging'

urlpatterns = [
    path('', ProcessList.as_view(), name="index")
]
