# from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    context = dict()
    context['hello'] = 'Hello World! Good afternoon'
    return render(request, 'hello.html', context)