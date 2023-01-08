def required_fields(request, *args):
    if request.method == 'GET':
        request_data = request.GET.dict()
    else:
        request_data = request.POST.dict()
    if args:
        for item in args:
            if item not in request_data:
                return False
        return True
