from django.shortcuts import HttpResponse, render


# Create your views here.
def home(request):
    return HttpResponse('init in site')


def mines_render(requests):
    return HttpResponse('init in mines')

