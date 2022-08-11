from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view



@api_view()
def product_list(request):
    return Response('Ok 200');


@api_view()
def product_view(request, id):
    return Response(f"product_id={id}")

