from django.urls import path
from .import views
from .views import hello_world

urlpatterns = [
    path('', hello_world, name='hello_world'),
]