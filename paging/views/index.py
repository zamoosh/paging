from .imports import *


class Index(View):
    def get(self, request):
        return render(request, 'index.html')

    def post(self, request):
        context = {}

        Process.clear_table()
        Log.clear_table()

        memory = int(request.POST.get('memory'))
        page_size = int(request.POST.get('page_size'))
        memory_object = Memory.get_memory()

        memory_object.size = memory
        memory_object.page_count = math.floor(memory / page_size)
        memory_object.left_page = memory_object.page_count
        memory_object.page_size = page_size

        process_array = Process.generate_process()

        not_completed = Process.objects.exclude(status__icontains='D').exists()
        time = 0
        main_log = []
        while not_completed:
            for process in process_array:
                if process.status == "D":
                    continue
                page_per_process = math.ceil(process.memory / page_size)
                if process.status == "P":
                    process.duration -= 1
                if process.duration == 0:
                    process.status = "D"
                if memory_object.left_page > page_per_process and process.status == "NS":
                    process.page_count = page_per_process
                    memory_object.left_page -= page_per_process
                    process.status = "P"

            Process.clear_table()
            process_array = Process.update_process(process_array)
            Log.objects.create(
                time=time,
                content=Process.get_json_data()
            )
            time_log = {
                'time': time,
                'left_memory': memory_object.left_page * memory_object.page_size,
                'total_memory': memory_object.size,
                'used_memory': (memory_object.page_count - memory_object.left_page) * memory_object.page_size
            }
            main_log.append(time_log)

            time += 1
            not_completed = Process.objects.exclude(status__icontains='D').exists()
            if not not_completed:
                memory_object.left_page = memory_object.page_count
                Log.objects.create(
                    time=time,
                    content=Process.get_json_data()
                )
                time_log = {
                    'time': time,
                    'left_memory': memory_object.left_page * memory_object.page_size,
                    'total_memory': memory_object.size,
                    'used_memory': (memory_object.page_count - memory_object.left_page) * memory_object.page_size
                }
                main_log.append(time_log)

        context['main_log'] = main_log
        return render(request, 'process_list.html', context)
