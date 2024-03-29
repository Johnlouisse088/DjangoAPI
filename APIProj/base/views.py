from django.http import HttpResponse


def hello(request):
    return HttpResponse("http://127.0.0.1:8000/api/")