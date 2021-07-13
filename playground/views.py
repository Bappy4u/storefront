from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import F
from store.models import Product, OrderItem, Order


def hello(request):

    querysets = Order.objects.select_related(
        'customer').prefetch_related('orderitem_set__product').order_by('-placed_at')[:5]

    return render(request, 'hello.html', {'orders': querysets})
