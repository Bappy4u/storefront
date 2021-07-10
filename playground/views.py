from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product


def hello(request):
    product = Product.objects.filter(pk=5).first()

    return render(request, 'hello.html', {'product': product})
