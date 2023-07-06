from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'mines/home.html')


def mines_render(requests):
    return render(requests, 'mines.html')

