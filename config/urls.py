from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from gar.views import MarcaViewSet

router = DefaultRouter()
router.register(r"marcas", MarcaViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]