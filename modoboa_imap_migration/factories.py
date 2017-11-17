"""IMAP migration factories."""

import factory

from modoboa.admin import factories as admin_factories

from . import models


class MigrationFactory(factory.DjangoModelFactory):
    """Factory for Migration."""

    class Meta:
        model = models.Migration

    mailbox = factory.SubFactory(admin_factories.MailboxFactory)
