"""API viewsets."""

from rest_framework import filters, permissions, viewsets

from . import models
from . import serializers


class EmailProviderViewSet(viewsets.ModelViewSet):
    """ViewSet class for EmailProvider."""

    filter_backends = (filters.SearchFilter, )
    permission_classes = (
        permissions.IsAuthenticated,
        permissions.DjangoModelPermissions
    )
    queryset = models.EmailProvider.objects.all().prefetch_related("domains")
    search_fields = ('name', )
    serializer_class = serializers.EmailProviderSerializer
