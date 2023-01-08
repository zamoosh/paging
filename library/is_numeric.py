def is_numeric(request, *fields):
    if request.method == 'GET':
        request_data = request.GET.dict()
    else:
        request_data = request.POST.dict()
    for item in fields:
        if item in request_data:
            if not request_data[item].isdigit():
                return False
    return True
