# users/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet

router = DefaultRouter()
router.register(u'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]