"""AppConfig for IMAP migration."""

from django.apps import AppConfig


class IMAPMigrationConfig(AppConfig):
    """App configuration."""

    name = "modoboa_imap_migration"
    verbose_name = "Migration through IMAP for Modoboa"

    def ready(self):
        from . import checks  # noqa
        from . import handlers  # noqa
