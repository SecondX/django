#encoding=utf-8
from django.http import HttpResponse
from django import template
from django.template.loader import get_template
from django.shortcuts import render_to_response



def here(request):
    return HttpResponse('媽，我在這！')
def math(request, a, b):
    a = int(a)
    b = int(b)
    s, d, p, q = a+b, a-b, a*b, a/b
    return render_to_response('math.html', locals())

