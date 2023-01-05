from django.urls import path
from .views import *

app_name = 'paging'

urlpatterns = [
    path('', index, name="index"),
    path('paging/', paging, name='paging'),
    path('segmenting/', segmenting, name='segmenting'),

    path('process_list/', ProcessList.as_view(), name="process_list"),

    # page not found
    path('<url>/', index),
    path('<str>/', index)
]
