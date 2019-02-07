"""API urls."""

from rest_framework import routers

from . import viewsets


router = routers.SimpleRouter()
router.register(r"email-providers", viewsets.EmailProviderViewSet)

urlpatterns = router.urls
