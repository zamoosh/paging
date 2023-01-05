from .imports import *


class ProcessList(View):

    @staticmethod
    def get(request):
        return render(request, 'time_list.html')
