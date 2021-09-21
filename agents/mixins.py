from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect

# CUSTOM CREATED MIXIN. BACKEND ACCESS CHECKING.
class OrganiserAndLoginRequiredMixin(AccessMixin):
    """Verify that the current user is authenticated AND is an organiser."""
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_organiser:
            return redirect("leads:lead-list")
        return super().dispatch(request, *args, **kwargs)