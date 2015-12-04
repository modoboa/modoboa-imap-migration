"""
IMAP migration models.
"""

from django.db import models

from modoboa.admin.models import Mailbox
from modoboa.lib.cryptutils import encrypt, decrypt


class Migration(models.Model):

    """Represent mailboxes to migrate."""

    mailbox = models.ForeignKey(Mailbox)
    _password = models.CharField(max_length=100)

    def __unicode__(self):
        return self.mailbox.full_address

    @property
    def password(self):
        """Password getter."""
        return decrypt(self._password)

    @password.setter
    def password(self, value):
        """Password setter."""
        self._password = encrypt(value)
