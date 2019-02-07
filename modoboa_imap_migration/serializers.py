"""API serializers."""

from rest_framework import serializers

from . import models


class EmailProviderDomainSerializer(serializers.ModelSerializer):
    """Serializer class for EmailProviderDomain."""

    class Meta:
        fields = ("id", "name", "new_domain")
        model = models.EmailProviderDomain
        read_only_fields = ("id", )


class EmailProviderSerializer(serializers.ModelSerializer):
    """Serializer class for EmailProvider."""

    domains = EmailProviderDomainSerializer(many=True, required=False)

    class Meta:
        fields = "__all__"
        model = models.EmailProvider

    def create(self, validated_data):
        """Create provider and domains."""
        domains = validated_data.pop("domains", None)
        provider = models.EmailProvider.objects.create(**validated_data)
        if domains:
            to_create = []
            for domain in domains:
                to_create.append(models.EmailProviderDomain(
                    provider=provider, **domain))
            models.EmailProviderDomain.objects.bulk_create(to_create)
        return provider

    def update(self, instance, validated_data):
        """Update provider and domains."""
        domains = validated_data.pop("domains", [])
        domain_ids = [domain.id for domain in domains]
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        for domain in instance.domains.all():
            if domain.id not in domain_ids:
                domain.delete()
            else:
                for updated_domain in domains:
                    if updated_domain.id != domain.id:
                        continue
                    domain.name = updated_domain.name
                    domain.new_domain = updated_domain.new_domain
                    domain.save()
                    break
        return instance
