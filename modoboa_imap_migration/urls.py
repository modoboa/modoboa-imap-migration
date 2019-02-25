"""Custom urls."""

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r"^$", views.IndexView.as_view(), name="index"),
    url(r"^migration/(?P<migration_pk>\d+)/delete/$", views.cancel_migration,
        name="migration_cancel"),
]
