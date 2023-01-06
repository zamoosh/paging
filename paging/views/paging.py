from .imports import *


def paging(request):
    context = {}

    if request.method == 'POST':

        Process.clear_table()
        Log.clear_table()

        process_count = None
        if request.POST.get('process_count'):
            process_count = int(request.POST.get('process_count'))
        memory = int(request.POST.get('memory'))
        page_size = int(request.POST.get('page_size'))
        memory_object = Memory.get_memory()

        memory_object.size = memory
        memory_object.page_count = math.floor(memory / page_size)
        memory_object.left_page = memory_object.page_count
        memory_object.page_size = page_size

        process_array = Process.generate_process(process_count)

        not_completed = Process.objects.exclude(status__icontains='D').exists()
        time = 0
        main_log = []
        logs = []
        while not_completed:
            for process in process_array:
                if process.status == "D":
                    continue
                page_per_process = math.ceil(process.memory / page_size)
                if process.status == "IP":
                    process.duration -= 1
                if process.duration == 0:
                    process.status = "D"
                    memory_object.left_page += process.page_count
                if memory_object.left_page >= page_per_process and process.status == "P":
                    process.page_count = page_per_process
                    process.page_used = page_per_process
                    memory_object.left_page -= page_per_process
                    process.status = "IP"
                    process.start_time = time

            Process.clear_table()
            process_array = Process.update_process(process_array)
            logs.append(Log(time=time, content=Process.get_json_data(paging=True), type='paging'))
            time_log = {
                'time': time,
                'left_memory': memory_object.left_page * memory_object.page_size,
                'left_page': memory_object.left_page,
                'used_memory': (memory_object.page_count - memory_object.left_page) * memory_object.page_size,
                'used_page': memory_object.page_count - memory_object.left_page
            }
            main_log.append(time_log)

            time += 1
            not_completed = Process.objects.exclude(status__icontains='D').exists()

        Log.objects.bulk_create(logs)
        context['main_log'] = main_log
        context['algorithm'] = 'Paging'
        context['total_memory'] = memory_object.size
        context['page_count'] = memory_object.page_count
        context['page_size'] = memory_object.page_size
        context['process_count'] = Process.process_count
        context['total_duration'] = time
        memory_object.save()
        return render(request, 'time_list.html', context)

    return render(request, 'paging.html')
