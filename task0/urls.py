from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('dbtest/', include('dbtest.urls')),
    path('admin/', admin.site.urls),
]