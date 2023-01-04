from .imports import *


def has_one_of_perms(perms):
    def decorator(function):
        def wrapper(request, *args, **kwargs):
            if any(request.user.has_perm(perm) for perm in perms):
                return function(request, *args, **kwargs)
            return redirect(reverse('page_not_found'))

        return wrapper

    return decorator
