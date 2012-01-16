from django.conf.urls.defaults import *

# Enable admin
from django.contrib import admin
admin.autodiscover()

# Enable static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Enable media
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Polls app
    url(r'^polls/', include('polls.urls')),
    
    # Admin
    url(r'^admin/', include(admin.site.urls)),
)

# Serve static
urlpatterns += staticfiles_urlpatterns()

# Serve media
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
