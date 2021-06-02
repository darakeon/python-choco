from django.urls import path, include
from rest_framework import routers
from .views import ChocolateViewSet

router = routers.DefaultRouter()
router.register(r'chocolate', ChocolateViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
