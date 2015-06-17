"""
Extension definition.
"""

from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _, ugettext_lazy

from modoboa.core.extensions import ModoExtension, exts_pool
from modoboa.lib import parameters, events

from .models import Migration


class ImapMigration(ModoExtension):

    """The ImapMigration extension class."""

    name = "modoboa_imap_migration"
    label = ugettext_lazy("IMAP migration using OfflineIMAP")
    version = "1.0.1"
    description = ugettext_lazy(
        "Migrate existing mailboxes using IMAP and OfflineIMAP"
    )

    def load(self):
        """Load extension."""
        from .app_settings import ParametersForm
        parameters.register(ParametersForm, _("IMAP migration"))

exts_pool.register_extension(ImapMigration)


@events.observe("ExtraAccountActions")
def extra_account_actions(account):
    """Add a link to disable the migration of this account."""
    if not account.mailbox_set.exists():
        return []
    migration = Migration.objects.filter(
        mailbox=account.mailbox_set.first()).first()
    if migration is not None:
        return [{
            "name": "cancel_migration",
            "url": reverse(
                "modoboa_imap_migration:migration_cancel", args=[migration.pk]
            ),
            "img": "fa fa-stop",
            "title": _("Cancel this account's migration"),
            "class": "ajaxcall",
            "confirm": _("Cancel the migration for %s?") % account,
            "extra_attributes": {
                "data-call_method": "DELETE"
            }
        }]
    return []
