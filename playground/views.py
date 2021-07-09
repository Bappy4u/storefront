from typing_extensions import ParamSpecKwargs
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product


def hello(request):
    try:
        product = Product.objects.get(pk=0)
    except ObjectDoesNotExist:
        pass

    return render(request, 'hello.html')
