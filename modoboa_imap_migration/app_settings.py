"""
Online settings for the IMAP migration.
"""
from django import forms
from django.utils.translation import ugettext_lazy as _

from modoboa.lib.parameters import AdminParametersForm
from modoboa.lib.form_utils import SeparatorField, YesNoField


class ParametersForm(AdminParametersForm):

    """IMAP migration settings."""

    app = "modoboa_imap_migration"

    sep1 = SeparatorField(label=_("Connection settings"))

    server_address = forms.CharField(
        label=_("Server address"),
        initial="127.0.0.1",
        help_text=_("Address of your IMAP server")
    )

    secured = YesNoField(
        label=_("Use a secured connection"),
        initial="no",
        help_text=_("Use a secured connection to access IMAP server")
    )

    server_port = forms.IntegerField(
        label=_("Server port"),
        initial=143,
        help_text=_("Listening port of your IMAP server")
    )

    sep2 = SeparatorField(label=_("OfflineIMAP settings"))

    max_sync_accounts = forms.IntegerField(
        label=_("Concurrent sync jobs"),
        initial=1,
        help_text=_("The maximum number of concurrent synchronization jobs")
    )
