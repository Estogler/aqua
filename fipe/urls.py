from .views import register_view
from django.urls import path

app_name = 'usuarios'

urlpatterns = [
    path('', register_view , name= 'criar'),
]