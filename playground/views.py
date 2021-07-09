from django.shortcuts import render
from store.models import Product


def hello(request):

    return render(request, 'hello.html')
