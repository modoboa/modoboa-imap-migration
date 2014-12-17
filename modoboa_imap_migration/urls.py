"""Custom urls."""

from django.conf.urls import patterns, url

urlpatterns = patterns(
    "modoboa_imap_migration.views",

    url(r"^migration/(?P<migration_pk>\d+)/delete/'$", "cancel_migration",
        name="migration_cancel"),
)
