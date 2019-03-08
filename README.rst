Mailboxes migration using OfflineIMAP
=====================================

|travis| |codecov| |landscape|

A simple `Modoboa <http://modoboa.org/>`_ extension which provides a
way to migrate existing mailboxes using `OfflineIMAP
<http://offlineimap.org/>`_.

How does it work
----------------

This extension mainly provides a cron script which periodically
synchronize user mailboxes from an existing IMAP server to a new
one. The workflow is pretty simple:

* A user from the old server logs into Modoboa using the same credentials

* A new account is automatically created and a new migration task is
  created using the provided credentials

* The cron script periodically synchronizes mailboxes corresponding to
  migration tasks

* Once a migration is done, it can be disabled through the admin panel

Installation
------------

Install this extension system-wide or inside a virtual environment by
running the following command::

  $ python setup.py install

Then, edit the ``settings.py`` file of your modoboa instance and
add ``modoboa_imap_migration`` inside the ``MODOBOA_APPS`` variable
like this::

  MODOBOA_APPS = (
    # ...
    'modoboa_imap_migration',
  )

Then, add the following at the end of the file::

  from modoboa_imap_migration import settings as modoboa_imap_migration_settings
  modoboa_imap_migration_settings.apply(globals())

Restart the python process running modoboa (uwsgi, gunicorn, apache,
whatever).

Run the following commands to setup the database tables::

  $ cd <modoboa_instance_dir>
  $ python manage.py migrate modoboa_imap_migration
  $ python manage.py load_initial_data

You also need to `install <http://offlineimap.org/doc/installation.html>`_ OfflineIMAP.

Configuration
-------------

Authentication backend
======================

.. warning::

   Please make sure automatic domain/mailbox creation is enabled,
   otherwise the authentication won't work. Go to the online settings
   panel (admin tab) and check your current state.

An IMAP authentication backend is provided by the extension and must
be enabled.

Edit the ``settings.py`` file and modify the
``AUTHENTICATION_BACKENDS`` variable as follows:

.. sourcecode:: python

  AUTHENTICATION_BACKENDS = (
      'django.contrib.auth.backends.ModelBackend',
      'modoboa_imap_migration.auth_backends.IMAPBackend',
  )

cron script
===========

The synchronization script must be configured to run periodically on
your new server. Since it will copy mailboxes content to its final
destination, filesystem permissions must be respected. To do that, it
must be executed by the user which owns mailboxes (generally
``vmail``).

Here is a configuration example where the script is executed every
hours. You can copy it inside the ``/etc/cron.d/modoboa`` file:

.. sourcecode:: shell

  PYTHON=/srv/modoboa/env/bin/python
  INSTANCE=/srv/modoboa/instance

  0       */1     *       *       *       vmail   cd /srv/vmail && $PYTHON $INSTANCE/manage.py generate_offlineimap_config --output .offlineimaprc && /usr/local/bin/offlineimap > /dev/null 2>&1

Feel free to adapt it.

Helper script for OfflineIMAP
=============================

OfflineIMAP will need a way to retrieve user passwords of the old
server. To do that, just copy the following Python code into a file
called ``.offlineimap.py``:

.. sourcecode:: python

  import os
  import site
  import sys

  site.addsitedir("/srv/modoboa/env/lib/python2.7/site-packages")
  sys.path.append("/srv/modoboa/instance")
  os.environ["DJANGO_SETTINGS_MODULE"] = "instance.settings"

  from django.apps import apps
  from django.conf import settings
  apps.populate(settings.INSTALLED_APPS)

  from modoboa_imap_migration.models import Migration

  def get_user_password(username):
      """Retrieve a password from Modoboa's database."""
      return Migration.objects.select_related().get(
          mailbox__user__username=username
      ).password

Then, copy this file into the home directory of the user owning
mailboxes (generally ``vmail``). For example:

.. sourcecode:: shell

  $ cp .offlineimap.py /srv/vmail
  $ chown vmail:vmail /srv/vmail/.offlineimap.py

Online settings
===============

You need to configure the access to the old IMAP server.

All the configuration is done from the admin panel (*Modoboa >
Parameters > IMAP migration*).

.. |landscape| image:: https://landscape.io/github/modoboa/modoboa-imap-migration/master/landscape.svg?style=flat
   :target: https://landscape.io/github/modoboa/modoboa-imap-migration/master
   :alt: Code Health

.. |travis| image:: https://travis-ci.org/modoboa/modoboa-imap-migration.svg?branch=master
   :target: https://travis-ci.org/modoboa/modoboa-imap-migration

.. |codecov| image:: https://codecov.io/gh/modoboa/modoboa-imap-migration/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/modoboa/modoboa-imap-migration
