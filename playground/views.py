from django.shortcuts import render


def cal(x, y):
    return x+y


def hello(request):
    sum = cal(2, 5)
    return render(request, 'hello.html')
