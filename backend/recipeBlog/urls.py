from django.conf.urls.static import static
from os import stat
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    #them tat ca url cua app blog_api 
    path('api/', include('blog_api.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
