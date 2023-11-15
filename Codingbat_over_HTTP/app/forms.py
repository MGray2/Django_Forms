from django import forms


class font_times_form(forms.Form):
    word = forms.CharField(max_length=30, min_length=3)
    times = forms.IntegerField()


class no_teen_sum_form(forms.Form):
    a = forms.IntegerField()
    b = forms.IntegerField()
    c = forms.IntegerField()


class xyz_there_form(forms.Form):
    word = forms.CharField(max_length=20)


class centered_average_form(forms.Form):
    a = forms.IntegerField()
    b = forms.IntegerField()
    c = forms.IntegerField()
    d = forms.IntegerField()
    e = forms.IntegerField()
    f = forms.IntegerField(required=False)
    g = forms.IntegerField(required=False)
