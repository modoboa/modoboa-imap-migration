"""
IMAP migration models.
"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from modoboa.admin.models import Mailbox
from modoboa.lib.cryptutils import encrypt, decrypt


@python_2_unicode_compatible
class Migration(models.Model):
    """Represent mailboxes to migrate."""

    mailbox = models.ForeignKey(Mailbox, on_delete=models.CASCADE)
    _password = models.CharField(max_length=255)

    def __str__(self):
        return self.mailbox.full_address

    @property
    def password(self):
        """Password getter."""
        return decrypt(self._password)

    @password.setter
    def password(self, value):
        """Password setter."""
        self._password = encrypt(value)
