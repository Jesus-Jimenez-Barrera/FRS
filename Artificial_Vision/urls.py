from django.urls import include, path
from . import views

urlpatterns = [
    path('capture/', views.capture_image, name='capture_image'),
]