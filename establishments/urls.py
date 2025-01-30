from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  
    path('upload/', views.upload_establishment, name='upload_establishment'),
    path('list/', views.list_establishments, name='list_establishments'),
]