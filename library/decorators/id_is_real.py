from .imports import *


def id_is_real(model, backward_url='/'):
    def decorator(function):
        def wrapper(request, obj_id, *args, **kwargs):
            if model.objects.filter(id=obj_id).exists():
                return function(request, obj_id, *args, **kwargs)
            try:
                reverse('page_not_found')  # check if page_not_found path exists or not.
                return redirect(reverse(
                    'page_not_found',
                    kwargs={'text': 'آی‌دی مورد‌نظر وجود ندارد!', 'backward_url': str(backward_url)}
                ))
            except (django.urls.exceptions.NoReverseMatch, Exception):
                return HttpResponse('آی‌دی موردنظر شما یافت نشد!')

        return wrapper

    return decorator
