from .imports import *


class ProcessList(View):

    @staticmethod
    def get(request):
        return render(request, 'process_list.html')
