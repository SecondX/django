#encoding=utf-8
from django.http import HttpResponse
from django import template
from django.template.loader import get_template



def here(request):
    return HttpResponse('媽，我在這！')
def math(request, a, b):
    a = int(a)
    b = int(b)
    s, d, p, q = a+b, a-b, a*b, a/b

    t = get_template('math.html')
    content = template.Context({'s':s, 'd':d, 'p':p, 'q':q})
    return HttpResponse(t.render(content))
