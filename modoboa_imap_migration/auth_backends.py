"""
IMAP authentication backend for Django.
"""
import imaplib
import socket
import ssl

from django.utils.translation import ugettext as _

from modoboa.core.models import User, populate_callback
from modoboa.lib import parameters
from modoboa.lib.exceptions import ModoboaException

from .models import Migration


class IMAPBackend(object):

    """IMAP authentication backend."""

    def authenticate(self, username=None, password=None):
        """Check the username/password and return a User."""
        if type(username) is unicode:
            username = username.encode("utf-8")
        if type(password) is unicode:
            password = password.encode("utf-8")
        address = parameters.get_admin("SERVER_ADDRESS")
        port = int(parameters.get_admin("SERVER_PORT"))
        try:
            if parameters.get_admin("SECURED") == "yes":
                conn = imaplib.IMAP4_SSL(address, port)
            else:
                conn = imaplib.IMAP4(address, port)
        except (socket.error, imaplib.IMAP4.error, ssl.SSLError) as error:
            raise ModoboaException(
                _("Connection to IMAP server failed: %s" % error))

        try:
            typ, data = conn.login(username, password)
        except imaplib.IMAP4.error:
            typ = "NO"
        conn.logout()
        if typ != "OK":
            return None
        return self.get_or_create_user(username, password)

    def get_or_create_user(self, username, password):
        """Get a user or create it the first time.

        .. note::

           We assume the username is a valid email address.
        """
        user, created = User.objects.get_or_create(
            username__iexact=username, defaults={
                "username": username.lower(), "email": username.lower()
            }
        )
        if created:
            user.set_password(password)
            user.save()
            populate_callback(user)
            Migration.objects.create(
                mailbox=user.mailbox_set.all()[0], password=password)
        return user

    def get_user(self, user_pk):
        """Retrieve a User instance."""
        user = None
        try:
            user = User.objects.get(pk=user_pk)
        except User.DoesNotExist:
            pass
        return user
