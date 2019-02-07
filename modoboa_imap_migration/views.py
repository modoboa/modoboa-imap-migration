"""Views for the IMAP migration extension."""

from django.utils.translation import ugettext as _

from django.contrib.auth import mixins as auth_mixins
from django.contrib.auth.decorators import (
    login_required, permission_required
)
from django.views import generic

from modoboa.lib.web_utils import render_to_json_response

from .models import Migration


class IndexView(auth_mixins.LoginRequiredMixin, generic.TemplateView):
    """Index view."""

    template_name = "modoboa_imap_migration/index.html"


@login_required
@permission_required("modoboa_imap_migraton.delete_migration")
def cancel_migration(request, migration_pk):
    """Cancel a migration."""
    try:
        migration = Migration.objects.get(pk=migration_pk)
    except Migration.DoesNotExist:
        return render_to_json_response(
            {"respmsg": _("Unknow migration")}, status=404
        )
    migration.delete()
    return render_to_json_response({
        "respmsg": _("Migration cancelled successfully")
    })
