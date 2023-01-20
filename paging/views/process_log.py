from .imports import *


def process_log(request, time):
    context = {}
    log = Log.get_object(time=time)
    if log:
        memory = Memory.get_memory()
        context['memory'] = memory
        if log.type.lower() == 'paging':  # algorith is paging
            context['page_count'] = memory.page_count
            context['page_size'] = memory.page_size
            context['page_used'] = memory.page_count - memory.left_page
        context['log'] = log
        context['process_count'] = Process.process_count

        prev_log = Log.objects.filter(time__lt=time).last()
        next_log = Log.objects.filter(time__gt=time).first()
        # get the previous log
        if prev_log:
            context['prev_log'] = prev_log.time
        # get the next log
        if next_log:
            context['next_log'] = next_log.time
        return render(request, 'process_log.html', context)
    return redirect(reverse('paging:index'))
