from django.urls import path, include

app_name = 'paging'

urlpatterns = [
    path('paging/', include('paging.views.urls')),
]
