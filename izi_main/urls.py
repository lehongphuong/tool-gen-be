from django.contrib import admin
from django.urls import path, include

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('jet/', include('jet.urls','jet')), # JET URLS  
    path('jet/dashboard/', include('jet.dashboard.urls','jet-dashboard')), # Django JET dashboard URLS
    path('admin/', admin.site.urls), 
    path('api/', include('apps.sample.urls')),
]


from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.OUTPUT_URL, document_root=settings.OUTPUT_ROOT)
