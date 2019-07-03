from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from ambulance_details import urls as AmbUrl
from api import urls as apiUrl
from accounts import urls as accUrl

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(apiUrl)),
    path('', include(AmbUrl)),
    path('account/', include(accUrl))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)