"""IMAP migration tests."""

import os
import shutil
import tempfile

import mock
from six.moves import configparser

from django.core.management import call_command
from django.urls import reverse

from modoboa.admin import factories as admin_factories
from modoboa.admin import models as admin_models
from modoboa.core import models as core_models
from modoboa.lib.tests import ModoTestCase

from . import factories
from . import models


class DataMixin(object):
    """A mixin to provide test data."""

    @classmethod
    def setUpTestData(cls):
        super(DataMixin, cls).setUpTestData()
        admin_factories.populate_database()
        cls.mb = admin_models.Mailbox.objects.get(
            user__username="user@test.com")
        cls.migration = factories.MigrationFactory(
            password="Toto1234", mailbox=cls.mb)


class ViewsTestCase(DataMixin, ModoTestCase):
    """Views test cases."""

    def test_extra_menu_entry(self):
        """Check that menu entry is added."""
        url = reverse("admin:_identity_list")
        response = self.ajax_get(url)
        cancel_url = reverse(
            "modoboa_imap_migration:migration_cancel",
            args=[self.migration.pk])
        self.assertIn(cancel_url, response["rows"])

    def test_cancel_migration(self):
        """Test cancel migration view."""
        cancel_url = reverse(
            "modoboa_imap_migration:migration_cancel",
            args=[self.migration.pk])
        self.ajax_delete(cancel_url)
        with self.assertRaises(models.Migration.DoesNotExist):
            self.migration.refresh_from_db()
        cancel_url = reverse(
            "modoboa_imap_migration:migration_cancel",
            args=[1000])
        self.ajax_delete(cancel_url, status=404)


class AuthenticationTestCase(ModoTestCase):
    """IMAP authentication test case."""

    @mock.patch("imaplib.IMAP4")
    def test_authentication(self, mock_imap):
        """Check IMAP authentication."""
        mock_imap.return_value.login.return_value = ["OK", b""]
        url = reverse("core:login")
        data = {"username": "new_user@test.com", "password": "Toto1234"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
        user = core_models.User.objects.get(username="new_user@test.com")
        self.assertEqual(user.mailbox.domain.name, "test.com")

        mock_imap.return_value.login.return_value = ["NO", b"Error"]
        data = {"username": "new_user@test.com", "password": "Toto123"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 401)


class ManagementCommandTestCase(DataMixin, ModoTestCase):
    """Management command test cases."""

    def setUp(self):
        super(ManagementCommandTestCase, self).setUp()
        self.workdir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.workdir)

    def test_generate_offlineimap_config(self):
        """Test generate_offlineimap_config command."""
        path = os.path.join(self.workdir, "offlineimap.conf")
        call_command("generate_offlineimap_config", "--output", path)
        self.assertTrue(os.path.exists(path))
        conf = configparser.ConfigParser()
        conf.read(path)
        self.assertTrue(conf.has_section("Account user@test.com"))
