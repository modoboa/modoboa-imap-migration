"""
Extension definition.
"""

from django.utils.translation import ugettext as _, ugettext_lazy

from modoboa.core.extensions import ModoExtension, exts_pool
from modoboa.lib import parameters


class ImapMigration(ModoExtension):

    """The ImapMigration extension class."""

    name = "modoboa_imap_migration"
    label = ugettext_lazy("IMAP migration using OfflineIMAP")
    version = "1.0"
    description = ugettext_lazy(
        "Migrate existing mailboxes using IMAP and OfflineIMAP"
    )

    def load(self):
        """Load extension."""
        from .app_settings import ParametersForm
        parameters.register(ParametersForm, _("IMAP migration"))

    def destroy(self):
        """Destroy extension (unload)."""
        parameters.unregister()

exts_pool.register_extension(ImapMigration)
