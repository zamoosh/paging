from .imports import *


class Index(View):
    def get(self, request):
        return render(request, 'index.html')

    def post(self, request):
        memory = request.POST.get('memory')
        page_size = request.POST.get('page_size')
        if memory and page_size:
            self.clear_database()
            self.generate_process()
        print(memory, page_size)
        return HttpResponse('welam kon ')

    def clear_database(self):
        Process.clear_process()
        Memory.clear_memory()
        Pages.clear_pages()

    def generate_process(self):
        process_array = []
        # for i in range(10000):
        #     # Process.objects.create(memory=10, duration=10)
        #     print(i)
        for i in Process.objects.all():
            print(i)
            # process_array.append(Process(memory=10, duration=10))

        # process_array = list(Process.objects.all())
        # for i in range(10000):
        #     some actions
            pass
        self.clear_database()





    def total_memory_gtn_process(self):
        pass
