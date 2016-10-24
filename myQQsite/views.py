#encoding=utf-8
from django.http import HttpResponse
from django import template

def here(request):
    return HttpResponse('媽，我在這！')
def math(request, a, b):
    a = int(a)
    b = int(b)
    s, d, p, q = a+b, a-b, a*b, a/b

    with open('templates/math.html', 'r') as reader:
        t = template.Template(reader.read())
    content = template.Context({'s':s, 'd':d, 'p':p, 'q':q})
    return HttpResponse(t.render(content))
