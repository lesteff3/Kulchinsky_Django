from django.urls import path
from cw20.views import lines, read

urlpatterns = [

    path('lines/', lines, name='lines'),
    path('read/', read, name='blog')


]