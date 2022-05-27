from django.contrib import admin
from django.urls import path, include

from some_app.views import index



urlpatterns = [
    path('admin/', admin.site.urls),
    path('some_app/', include('some_app.urls')),
]
