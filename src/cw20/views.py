
from django.http import HttpResponse

from django.shortcuts import render

from cw20.forms import WriteLinesForm


def lines(request):
    submit_button = request.POST.get("submit")

    firstname = ''
    lastname = ''
    age = ''

    form = WriteLinesForm(request.POST or None)
    if form.is_valid():
        firstname = form.cleaned_data.get("first_name")
        lastname = form.cleaned_data.get("last_name")
        age = form.cleaned_data.get("age")

    context = {'form': form, 'firstname': firstname,
               'lastname': lastname, 'submit_button': submit_button,
               'age': age}
    return render(request, 'write_lines_form.html', context=context)


def read(request):
    if request.method == "GET":
        submit_button = request.GET.get("submit")
        firstname = request.GET.get("first_name")
        lastname = request.GET.get("last_name")
        age = request.GET.get("age")
        context = {'firstname': firstname,
                   'lastname': lastname, 'submit_button': submit_button,
                   'age': age}
        return render(request, 'read.html', context=context)

