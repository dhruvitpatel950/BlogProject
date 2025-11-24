from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from home.views import *

from blogs.views import *

urlpatterns = [
    path('', home, name = 'home'),
    path('admin/', admin.site.urls),
    path('contact/', contact, name = 'contact'),
    path('about/', about, name = 'about'),
    path('blog/', include('blogs.urls')),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
