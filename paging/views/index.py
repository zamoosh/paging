from .imports import *


class Index(View):
    def get(self, request):
        return render(request, 'index.html')

    def post(self, request):
        Process.clear_table()
        Log.clear_table()

        memory = int(request.POST.get('memory'))
        page_size = int(request.POST.get('page_size'))
        memory_object = Memory.get_memory()

        memory_object.memory = memory
        memory_object.page_count = math.floor(memory / page_size)
        memory_object.left_page = memory_object.page_count

        process_array = Process.generate_process()

        not_completed = Process.objects.exclude(status__icontains='D').exists()
        time = 0
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
            time += 1
            not_completed = Process.objects.exclude(status__icontains='D').exists()

        return HttpResponse('salam man be to yar ghadimi!!')
