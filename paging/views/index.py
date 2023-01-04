from .imports import *


class Index(View):
    def get(self, request):
        return render(request, 'index.html')
