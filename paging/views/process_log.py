from .imports import *


def process_log(request, time):
    context = {}
    log = Log.get_object(time=time)
    if log:
        context['log'] = log
        return render(request, 'process_log.html', context)
    return redirect(reverse('paging:index'))
