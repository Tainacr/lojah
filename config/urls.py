from django.contrib import admin
from django.urls import path
from django.contrib import admin
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name="index"),
]
