from .imports import *


def segmenting(request):
    context = {}
    if request.method == 'POST' and required_fields(request, 'memory'):
        Process.clear_table()
        Log.clear_table()

        process_count = None
        if request.POST.get('process_count'):
            try:
                process_count = int(request.POST.get('process_count'))
            except (ValueError, Exception):
                return redirect(reverse('paging:segmenting'))
        if not is_numeric(request, 'memory'):
            return redirect(reverse('paging:segmenting'))
        memory = int(request.POST.get('memory'))
        if memory <= 1:
            return redirect(reverse('paging:segmenting'))
        memory_object = Memory.get_memory()

        memory_object.size = memory
        memory_object.left_memory = memory

        process_array = Process.generate_process(process_count)

        not_completed = Process.objects.exclude(Q(status__icontains='D') | Q(status__icontains='T')).exists()
        time = 0
        main_log = []
        logs = []
        while not_completed:
            for process in process_array:
                if process.status == "D" or process.status == "T":
                    continue
                if process.status == "IP":
                    process.duration -= 1
                if process.duration == 0:
                    process.status = "D"
                    memory_object.left_memory += process.memory
                if memory_object.left_memory >= process.memory and process.status == "P":
                    memory_object.left_memory -= process.memory
                    process.status = "IP"
                    process.start_time = time
                if memory_object.page_count < process.memory and process.status == "P":
                    process.status = 'T'

            Process.clear_table()
            process_array = Process.update_process(process_array)
            logs.append(Log(time=time, content=Process.get_json_data(), type='segmenting'))
            time_log = {
                'time': time,
                'left_memory': memory_object.left_memory,
                'total_memory': memory_object.size,
                'used_memory': (memory_object.size - memory_object.left_memory)
            }
            main_log.append(time_log)

            time += 1
            not_completed = Process.objects.exclude(Q(status__icontains='D') | Q(status__icontains='T')).exists()
        Log.objects.bulk_create(logs)
        context['main_log'] = main_log
        context['algorithm'] = 'Segmenting'
        context['total_memory'] = memory_object.size
        context['process_count'] = Process.process_count
        context['total_duration'] = time
        memory_object.save()
        return render(request, 'time_list.html', context)

    return render(request, 'segmenting.html')
