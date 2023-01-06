from .imports import *


def segmenting(request):
    context = {}
    if request.method == 'POST':
        Process.clear_table()
        Log.clear_table()

        process_count = None
        if request.POST.get('process_count'):
            process_count = int(request.POST.get('process_count'))
        memory = int(request.POST.get('memory'))
        memory_object = Memory.get_memory()

        memory_object.size = memory
        memory_object.left_memory = memory

        process_array = Process.generate_process(process_count)

        not_completed = Process.objects.exclude(status__icontains='D').exists()
        time = 0
        main_log = []
        logs = []
        while not_completed:
            for process in process_array:
                if process.status == "D":
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
            not_completed = Process.objects.exclude(status__icontains='D').exists()
        Log.objects.bulk_create(logs)
        context['main_log'] = main_log
        context['algorithm'] = 'Segmenting'
        context['total_memory'] = memory_object.size
        context['process_count'] = Process.process_count
        context['total_duration'] = time
        memory_object.save()
        return render(request, 'time_list.html', context)

    return render(request, 'segmenting.html')
