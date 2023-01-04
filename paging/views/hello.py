from django.http import HttpResponse
from django.views.generic import View


class ProcessList(View):
    def get(self, request):
        return HttpResponse('hello here we go agian')


def hello(request):
    print('change')
    return HttpResponse('hello here we go agian')

