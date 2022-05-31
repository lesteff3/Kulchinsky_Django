from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include




urlpatterns = [

    path('admin/', admin.site.urls),
    path('some_app/', include('some_app.urls')),
    path('cw20/', include('cw20.urls')),
    path('cw21/', include('cw21.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
