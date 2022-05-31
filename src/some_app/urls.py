
from django.urls import path

from some_app.views import get_student

urlpatterns = [

    path('get_student/', get_student, name='get_student')



]
