
from django.http import HttpResponse
from django.template import loader, Template, Context


def get_student(request):
    first_name = request.GET.get('first_name')
    last_name = request.GET.ger('last_name')
    age = request.GET.get('age')
    comment = request.GET.get('comment')
    print(f'{first_name} {last_name} {age} {comment}')
    return HttpResponse(request)
