from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('chapters/', include('chapter.urls')),
    path('docs/', include('document.urls')),
    path('das/', include('faculty.urls')),
]
