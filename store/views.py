from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import response


def products(request):
    return HttpResponse('Ok 200');

