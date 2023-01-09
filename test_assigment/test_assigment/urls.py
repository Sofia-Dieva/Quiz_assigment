from django.contrib import admin
from django.template.defaulttags import url
from django.urls import path, include
import re

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls'), name='login'),
    path('', include('quiz_1.urls')),
    path('_nested_admin/', include('nested_admin.urls'))
]
