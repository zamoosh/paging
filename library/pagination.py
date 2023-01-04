from django.core.paginator import *


class Pagination:
    """
    * sample use:
        page = Pagination(request, queryset, 1, 10)

    * attrs:
        - page.page_url: The current url we are in.
        - page.objects: Our model object we passed in 'queryset'. We can iterate over it to show objects.
        - page.page: Number of the target page.
        - page.limit: How much object per each page.
        - page.queryset: The queryset of model object we passed.
        - page.request: The Django request using in views.
    """

    def __init__(self, request, queryset, page=1, limit=10):
        if page <= 0 or limit <= 0:
            raise ValueError('Please enter a positive int number for "page" or "limit"')
        self.request = request
        self.queryset = queryset
        self.page = page
        self.limit = limit
        self._get_page_url()
        self._get_page()

    def _get_page_url(self):
        """set the current url to 'self.page_url' used in pagination.html template"""
        self.page_url = self.request.build_absolute_uri().split('?')[0]

    def _get_page(self):
        """self.objects is the page object containing 'our model' objects"""
        limit = self.request.GET.get('limit')
        if limit:
            try:
                self.limit = int(limit)
            except (ValueError, Exception):
                pass
        self.paginator = Paginator(self.queryset, self.limit)
        try:
            page = int(self.request.GET.get('page_number'))
            if page and page > 1:
                self.objects = self.paginator.get_page(page)
            else:
                self.objects = self.paginator.get_page(self.page)
        except (ValueError, Exception):
            self.objects = self.paginator.get_page(self.page)
