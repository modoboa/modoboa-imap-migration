"""Views for the IMAP migration extension."""

from django.contrib.auth import mixins as auth_mixins

from django.views import generic


class IndexView(auth_mixins.LoginRequiredMixin,
                auth_mixins.PermissionRequiredMixin,
                generic.TemplateView):
    """Index view."""

    permission_required = "modoboa_imap_migration.add_migration"
    template_name = "modoboa_imap_migration/index.html"

    def get_context_data(self, **kwargs):
        """Set menu selection."""
        kwargs.update({"selection": "imap_migrations"})
        return super(IndexView, self).get_context_data(**kwargs)
