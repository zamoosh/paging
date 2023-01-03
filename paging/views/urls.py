from django.urls import path, include
from .process import *

urlpatterns = [
    path('process/', include('paging.views.process.urls'))
]
