from django.http import HttpResponse
from django.views.generic import View
from .imports import *


class ProcessList(View):
    def get(self, request):
        return render(request, 'home.html')


def hello(request):
    print('change')
    return HttpResponse('hello here we go agian')
