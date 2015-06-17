"""
A management command to create an offlineimap configuration file.
"""

from optparse import make_option

from django.core.management.base import BaseCommand
from django.template.loader import render_to_string

from modoboa.lib import parameters

from modoboa_admin.modo_extension import AdminConsole

from ...modo_extension import ImapMigration
from ...models import Migration


class Command(BaseCommand):

    """Command definition."""

    help = "Generate an offlineimap configuration file."

    option_list = BaseCommand.option_list + (
        make_option("--output", default="/tmp/offlineimap.conf",
                    help="Path of the generated file"),
    )

    def handle(self, *args, **options):
        """Entry point."""
        AdminConsole().load()
        ImapMigration().load()

        context = {
            "imap_server_address": parameters.get_admin("SERVER_ADDRESS"),
            "imap_server_port": parameters.get_admin("SERVER_PORT"),
            "imap_server_secured": parameters.get_admin("SECURED"),
            "migrations": Migration.objects.select_related().all(),
        }
        with open(options["output"], "w") as fpo:
            content = render_to_string(
                "modoboa_imap_migration/offlineimap.conf", context)
            fpo.write(content)
