from django import forms


class WriteLinesForm(forms.Form):
    first_name = forms.CharField(min_length=2, max_length=20)
    last_name = forms.CharField(min_length=2, max_length=20)
    age = forms.IntegerField(min_value=0, max_value=80)
