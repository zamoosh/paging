from .imports import *


def process_log(request, time):
    context = {}
    log = Log.get_object(time=time)
    if log:
        memory = Memory.get_memory()
        if log.type.lower() == 'paging':  # algorith is paging
            context['page_count'] = memory.page_count
            context['page_size'] = memory.page_size
            context['page_used'] = memory.page_count - memory.left_page
            context['memory'] = memory
        context['log'] = log
        context['process_count'] = Process.process_count
        return render(request, 'process_log.html', context)
    return redirect(reverse('paging:index'))
