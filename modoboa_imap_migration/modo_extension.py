"""Extension definition."""

from django.utils.translation import ugettext as _, ugettext_lazy

from modoboa.core.extensions import ModoExtension, exts_pool
from modoboa.parameters import tools as param_tools

from . import __version__
from . import forms


class ImapMigration(ModoExtension):
    """The ImapMigration extension class."""

    name = "modoboa_imap_migration"
    label = ugettext_lazy("IMAP migration using OfflineIMAP")
    version = __version__
    description = ugettext_lazy(
        "Migrate existing mailboxes using IMAP and OfflineIMAP"
    )

    def load(self):
        """Load extension."""
        param_tools.registry.add(
            "global", forms.ParametersForm, _("IMAP migration"))

exts_pool.register_extension(ImapMigration)
