
from django.urls import path

from some_app.views import index, conclusion_commit, found_letters, name_person, first_name, create_name

urlpatterns = [

    path(r'index/', index, name='index'),
    path(r'found_letters/', found_letters, name='found_letters'),
    path(r'conclusion_commit/', conclusion_commit, name='conclusion_commit'),
    path(r'name_person/', name_person, name='name_person'),
    path(r'first_name/', first_name, name='first_name'),
    path(r'create_name/', create_name, name='create_name')

]
