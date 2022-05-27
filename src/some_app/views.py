from django.http import HttpResponse
from django.template import loader, Template, Context





def name_person(request):
    template = loader.get_template('index.html')
    context = {'name': 'Alex'}
    name = request.GET.get('name')
    if not name:
        return HttpResponse('Input your name in URL string!')
    return HttpResponse(f'Hello {name}')


def first_name(request):
    name = request.GET.get('name')
    return HttpResponse(f'{name}')


def index(request):
    first_name = request.GET.get('first_name')
    second_name = request.GET.get('second_name')
    age = request.GET.get('age')
    if not age or age and int(age) < 18:
        return HttpResponse(f'Permission denied!')
    return HttpResponse(f'Welcome {first_name} {second_name}!')


def conclusion_commit(request):
    first_name = request.GET.get('first_name')
    age = request.GET.get('age')
    commit = request.GET.get('commit')
    if not commit:
        return HttpResponse('No such commit')
    my_list = []
    for x in commit:
        my_list.append(f'{x} (c) {first_name}')
    return HttpResponse(f'{my_list}')


def found_letters(request):
    first_name = request.GET.get('first_name')
    second_name = request.GET.get('second_name')
    commit = request.GET.get('commit')
    if not commit:
        return HttpResponse('No such commit')
    word = "AEIOUaeiou"
    vowels = "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz"
    total = 0
    total_2 = 0
    for r in word:
        if r in commit:
            total += 1
    for w in vowels:
        if w in commit:
            total_2 += 1
    return HttpResponse(f'Длина коммита {len(commit)} : гласных = {total}, согласных = {total_2}')


def create_name(request):
    name = request.GET.get('name')
    if not name:
        name = input('Please input your name')
        return HttpResponse(f'{name}')







