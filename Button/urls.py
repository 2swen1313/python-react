from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from buttonapp.views import ButtonViewSet


router = DefaultRouter()
router.register('button', ButtonViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls))
]