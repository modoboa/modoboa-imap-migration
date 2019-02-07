"""IMAP migration handlers."""

from django.urls import reverse
from django.dispatch import receiver
from django.utils.translation import ugettext as _

from modoboa.core import signals as core_signals
from .models import Migration


@receiver(core_signals.extra_user_menu_entries)
def menu(sender, location, user, **kwargs):
    """Return extra menu entry."""
    if location != "top_menu" or not user.is_superuser:
        return []
    return [
        {"name": "imap_migrations",
         "label": _("IMAP migration"),
         "url": reverse("modoboa_imap_migration:index")}
    ]


@receiver(core_signals.extra_account_actions)
def extra_account_actions(sender, account, **kwargs):
    """Add a link to disable the migration of this account."""
    if not hasattr(account, "mailbox"):
        return []
    migration = Migration.objects.filter(mailbox=account.mailbox).first()
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
