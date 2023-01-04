from .imports import *


def is_admin(function):
    def wrapper(request, **kwargs):
        if request.user.is_superuser or request.user.is_staff:
            return function(request, **kwargs)
        return redirect(reverse('page_not_found'))

    return wrapper
