from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.models import User, Group
from rest_framework import routers, serializers, viewsets
from django.conf.urls.static import static
from django.conf import settings

from rest_framework import routers

from content_api.views import ItemViewSet

router = routers.DefaultRouter()
router.register(r'item', ItemViewSet, basename='item')


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'api/', include('api.urls',)),

    url(r'api/', include(router.urls)),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
