"""IMAP migration forms."""

from django import forms
from django.utils.translation import ugettext_lazy as _

from modoboa.lib import form_utils
from modoboa.parameters import forms as param_forms


class ParametersForm(param_forms.AdminParametersForm):
    """IMAP migration settings."""

    app = "modoboa_imap_migration"

    sep1 = form_utils.SeparatorField(label=_("Connection settings"))

    server_address = forms.CharField(
        label=_("Server address"),
        initial="127.0.0.1",
        help_text=_("Address of your IMAP server")
    )

    secured = form_utils.YesNoField(
        label=_("Use a secured connection"),
        initial=False,
        help_text=_("Use a secured connection to access IMAP server")
    )

    server_port = forms.IntegerField(
        label=_("Server port"),
        initial=143,
        help_text=_("Listening port of your IMAP server")
    )

    sep2 = form_utils.SeparatorField(label=_("OfflineIMAP settings"))

    max_sync_accounts = forms.IntegerField(
        label=_("Concurrent sync jobs"),
        initial=1,
        help_text=_("The maximum number of concurrent synchronization jobs")
    )

    sep2 = form_utils.SeparatorField(label=_("OfflineIMAP Filter settings"))

    create_folders = form_utils.YesNoField(
        label=_("Create Folders"),
        initial=True,
        help_text=_("Allow Creation of missing folders during sync")
    )

    folder_filter_exclude = forms.CharField(
        required=False,
        label=_("Folder Filter Exclusions"),
        initial="",
        help_text=_(
            "Use a regular expression to explicitly include folders in sync. "
            "Example: ^Trash$|Del"
        )
    )

    folder_filter_include = forms.CharField(
        required=False,
        label=_("Folder Filter Inclusions"),
        initial="",
        help_text=_(
            "A comma seperated list of folders to explicitly include in sync "
            "even if filtered by the Folder Filter Exclusions. Example: "
            "debian.user, debian.personal "
        )
    )
