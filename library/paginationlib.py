from django.core.paginator import *


class Paginationlib:
    def __init__(self, request, queryset, page=1, limit=10):
        self.queryset = queryset
        myqueryparam = {}
        myqueryparam.update(request.GET)
        paginator = Paginator(self.queryset, limit)

        try:
            self.queryset = paginator.page(page)
        except PageNotAnInteger:
            self.queryset = paginator.page(1)
        except EmptyPage:
            self.queryset = paginator.page(paginator.num_pages)
        try:
            del myqueryparam['page']
        except:
            pass

        self.queryset.queryparam = self.queryparam(myqueryparam)

    def pagination(self):
        return self.queryset

    def queryparam(self, mydict):
        stringret = "?"
        for key, value in mydict.items():
            for i in value:
                stringret += f"{key}={i}&"
        return stringret
