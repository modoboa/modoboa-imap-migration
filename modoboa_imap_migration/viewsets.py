"""API viewsets."""

from rest_framework import permissions, viewsets

from . import models
from . import serializers


class EmailProviderViewSet(viewsets.ModelViewSet):
    """ViewSet class for EmailProvider."""

    permission_classes = (
        permissions.IsAuthenticated,
        permissions.DjangoModelPermissions
    )
    queryset = models.EmailProvider.objects.all().prefetch_related("domains")
    serializer_class = serializers.EmailProviderSerializer
