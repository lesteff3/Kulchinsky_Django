from django.urls import path
from cw21 import views


urlpatterns = [
    path('home/', views.home_page, name='home'),
    path('create/', views.create, name='create'),


]