from django.http import HttpResponse

def index(request):
    return HttpResponse("Witam w indexie.")