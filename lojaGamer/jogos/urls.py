from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import JogosViewSet

router = DefaultRouter()
router.register(r'', JogosViewSet)
jogos_urls = router.urls
