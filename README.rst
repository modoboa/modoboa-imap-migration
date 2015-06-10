Mailboxes migration using OfflineIMAP
=====================================

|landscape|

A simple `Modoboa <http://modoboa.org/>`_ extension which provides a
way to migrate existing mailboxes using `OfflineIMAP
<http://offlineimap.org/>`_.

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

Restart the python process running modoboa (uwsgi, gunicorn, apache,
whatever).

Configuration
-------------

All the configuration is done from the admin panel (*Modoboa >
Parameters > IMAP migration*).

.. |landscape| image:: https://landscape.io/github/modoboa/modoboa-imap-migration/master/landscape.svg?style=flat
   :target: https://landscape.io/github/modoboa/modoboa-imap-migration/master
   :alt: Code Health
