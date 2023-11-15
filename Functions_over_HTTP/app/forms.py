from django import forms


class hey_you_form(forms.Form):
    user_name = forms.CharField()


class age_in_form(forms.Form):
    user_age = forms.IntegerField()
    end_year = forms.IntegerField()


class order_total_form(forms.Form):
    burgers = forms.IntegerField()
    fries = forms.IntegerField()
    drinks = forms.IntegerField()
