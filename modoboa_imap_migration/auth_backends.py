"""IMAP authentication backend for Django."""

import imaplib
import socket
import ssl

from django.utils.encoding import smart_bytes
from django.utils.translation import ugettext as _

from modoboa.core.models import User, populate_callback
from modoboa.lib import email_utils
from modoboa.lib.exceptions import ModoboaException

from . import models


class IMAPBackend(object):
    """IMAP authentication backend."""

    def authenticate(self, username=None, password=None):
        """Check the username/password and return a User."""
        self.address, domain = email_utils.split_mailbox(username)
        provider_domain = models.EmailProviderDomain.objects.filter(
            name=domain).select_related("provider").first()
        if not provider_domain:
            # Domain not allowed for migration: failure
            return None
        address = provider_domain.provider.address
        port = provider_domain.provider.port
        try:
            if provider_domain.provider.secured:
                conn = imaplib.IMAP4_SSL(address, port)
            else:
                conn = imaplib.IMAP4(address, port)
        except (socket.error, imaplib.IMAP4.error, ssl.SSLError) as error:
            raise ModoboaException(
                _("Connection to IMAP server failed: %s") % error)

        try:
            typ, data = conn.login(
                smart_bytes(username), smart_bytes(password))
        except imaplib.IMAP4.error:
            typ = "NO"
        conn.logout()
        if typ != "OK":
            return None
        self.provider_domain = provider_domain
        return self.get_or_create_user(username, password)

    def get_or_create_user(self, username, password):
        """Get a user or create it the first time.

        .. note::

           We assume the username is a valid email address.
        """
        orig_username = username
        # Check if old addresses must be converted
        if self.provider_domain.new_domain:
            username = u"{}@{}".format(
                self.address, self.provider_domain.new_domain.name)
        user, created = User.objects.get_or_create(
            username__iexact=username, defaults={
                "username": username.lower(), "email": username.lower()
            }
        )
        if created:
            user.set_password(password)
            user.save()
            populate_callback(user)
            models.Migration.objects.create(
                provider=self.provider_domain.provider,
                mailbox=user.mailbox,
                username=orig_username,
                password=password
            )
        return user

    def get_user(self, user_pk):
        """Retrieve a User instance."""
        user = None
        try:
            user = User.objects.get(pk=user_pk)
        except User.DoesNotExist:
            pass
        return user
