from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from manager.models import Book


def hello(request, name='igor', digit=None):
    if digit is not None:
        return HttpResponse(f'digit {digit}')
    return HttpResponse(f'hello world from {name}')

class MyBook(View):
    def get(self, request):
        context = {}
        context['books'] = Book.objects.all()
        return render(request, "index.html", context)