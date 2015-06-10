"""
Helpers for OfflineIMAP.
"""

import os
import site
import sys

site.addsitedir("")
sys.path.append("")
os.environ["DJANGO_SETTINGS_MODULE"] = ""

from modoboa.core import load_core_settings
from modoboa_imap_migration.models import Migration

load_core_settings()


def get_user_password(username):
    """Retrieve a password from Modoboa's database."""
    return Migration.objects.select_related().get(
        mailbox__user__username=username
    ).password
