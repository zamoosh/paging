from .imports import *


def index(request, keyword=None, url=None):
    return redirect(reverse('paging:paging'))
