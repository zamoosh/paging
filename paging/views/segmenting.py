from .imports import *


def segmenting(request):
    context = {}
    if request.method == 'POST':
        Process.clear_table()
        Log.clear_table()

        memory = int(request.POST.get('memory'))
        memory_object = Memory.get_memory()

        memory_object.size = memory
        memory_object.left_memory = memory

        process_array = Process.generate_process()

        not_completed = Process.objects.exclude(status__icontains='D').exists()
        time = 0
        main_log = []
        logs = []
        while not_completed:
            for process in process_array:
                if process.status == "D":
                    continue
                if process.status == "P":
                    process.duration -= 1
                if process.duration == 0:
                    process.status = "D"
                    memory_object.left_memory += process.memory
                if memory_object.left_memory >= process.memory and process.status == "NS":
                    memory_object.left_memory -= process.memory
                    process.status = "P"

            Process.clear_table()
            process_array = Process.update_process(process_array)
            logs.append(Log(time=time, content=Process.get_json_data()))
            # Log.objects.create(
            #     time=time,
            #     content=Process.get_json_data()
            # )
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
        return render(request, 'process_list.html', context)

    return render(request, 'segmenting.html')
