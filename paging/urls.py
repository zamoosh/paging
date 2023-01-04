from django.urls import path
from .views import *

app_name = 'paging'

urlpatterns = [
    path('', Index.as_view(), name="index"),
    path('process_list/', ProcessList.as_view(), name="process_list")
]
