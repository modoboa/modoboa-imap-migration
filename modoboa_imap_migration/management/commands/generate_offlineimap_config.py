"""A management command to create an offlineimap configuration file."""

from django.core.management.base import BaseCommand
from django.template.loader import render_to_string

from modoboa.admin.app_settings import load_admin_settings
from modoboa.parameters import tools as param_tools

from ...modo_extension import ImapMigration
from ...models import Migration


class Command(BaseCommand):
    """Command definition."""

    help = "Generate an offlineimap configuration file."

    def add_arguments(self, parser):
        """Add extra arguments to command line."""
        parser.add_argument(
            "--output", default="/tmp/offlineimap.conf",
            help="Path of the generated file")

    def handle(self, *args, **options):
        """Entry point."""
        load_admin_settings()
        ImapMigration().load()
        conf = dict(
            param_tools.get_global_parameters("modoboa_imap_migration"))
        context = {
            "imap_server_address": conf["server_address"],
            "imap_server_port": conf["server_port"],
            "imap_server_secured": conf["secured"],
            "migrations": Migration.objects.select_related("mailbox").all(),
        }
        with open(options["output"], "w") as fpo:
            content = render_to_string(
                "modoboa_imap_migration/offlineimap.conf", context)
            fpo.write(content)
