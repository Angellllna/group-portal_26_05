"""
Heist Academy — role-checking helpers.

Use these functions/decorators in ANY app to check the role of the
currently logged-in user. They are safe to call even for anonymous
users or users that don't have a Profile yet (always return False
in that case, never raise an exception).

    from accounts.permissions import is_cadet, is_instructor, is_admin_role
    from accounts.permissions import instructor_required, admin_required, role_required

Quick reference
---------------
is_cadet(user)        -> bool
is_instructor(user)   -> bool
is_admin_role(user)   -> bool

@role_required("instructor", "admin")   # allow several roles
@instructor_required                     # shortcut: instructor or admin
@admin_required                          # shortcut: admin only
"""

from functools import wraps

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect

from .models import Profile


# ---------------------------------------------------------------------------
# Plain helper functions — use these for conditional logic inside a view,
# a template ({% if %}), or anywhere else.
# ---------------------------------------------------------------------------

def get_role(user):
    """Returns the role string of a user's Profile, or None."""
    if not user or not user.is_authenticated:
        return None
    profile = getattr(user, "profile", None)
    return profile.role if profile else None


def is_cadet(user):
    return get_role(user) == Profile.Role.CADET


def is_instructor(user):
    return get_role(user) == Profile.Role.INSTRUCTOR


def is_admin_role(user):
    """Checks the Profile.role field (NOT Django's is_staff/is_superuser)."""
    return get_role(user) == Profile.Role.ADMIN


# Instructors and admins both get "instructor-level" access.
def has_instructor_access(user):
    return is_instructor(user) or is_admin_role(user)


# ---------------------------------------------------------------------------
# Decorators — use these on function-based views to restrict access.
# Each one already implies @login_required (anonymous users are sent
# to the login page first).
# ---------------------------------------------------------------------------

def role_required(*allowed_roles):
    """
    Generic decorator: allow access only to users whose Profile.role
    is in `allowed_roles`.

        @role_required("instructor", "admin")
        def create_event(request):
            ...
    """
    def decorator(view_func):
        @wraps(view_func)
        @login_required
        def wrapped(request, *args, **kwargs):
            if get_role(request.user) not in allowed_roles:
                messages.error(request, "You don't have permission to access this page.")
                raise PermissionDenied("Insufficient role.")
            return view_func(request, *args, **kwargs)
        return wrapped
    return decorator


def instructor_required(view_func):
    """Shortcut: allows instructors and admins."""
    @wraps(view_func)
    @login_required
    def wrapped(request, *args, **kwargs):
        if not has_instructor_access(request.user):
            messages.error(request, "Instructor access required.")
            raise PermissionDenied("Instructor access required.")
        return view_func(request, *args, **kwargs)
    return wrapped


def admin_required(view_func):
    """Shortcut: allows admins only."""
    @wraps(view_func)
    @login_required
    def wrapped(request, *args, **kwargs):
        if not is_admin_role(request.user):
            messages.error(request, "Admin access required.")
            raise PermissionDenied("Admin access required.")
        return view_func(request, *args, **kwargs)
    return wrapped