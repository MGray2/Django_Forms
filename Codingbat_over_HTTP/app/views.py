from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from app.forms import (
    font_times_form,
    no_teen_sum_form,
    xyz_there_form,
    centered_average_form,
)
import math


# Create your views here.
def landing_page(request: HttpRequest) -> HttpResponse:
    return render(request, "landing_page.html")


def front_times(request: HttpRequest) -> HttpResponse:
    form = font_times_form(request.GET)
    if form.is_valid():
        word = form.cleaned_data["word"]
        times = form.cleaned_data["times"]

        if len(word) < 3:
            return ""
        front = word[:3]

        result = ""
        for i in range(times):
            result = result + front
    else:
        result = ""
    return render(request, "form.html", {"result": result})


def no_teen_sum(request: HttpRequest) -> HttpResponse:
    form = no_teen_sum_form(request.GET)
    if form.is_valid():
        a = form.cleaned_data["a"]
        b = form.cleaned_data["b"]
        c = form.cleaned_data["c"]

        def fix_teen(n) -> int:
            if n == 15 or n == 16:
                return n
            elif n in range(13, 19):
                return 0
            else:
                return n

        result = fix_teen(a) + fix_teen(b) + fix_teen(c)
    else:
        result = None
    return render(request, "form_2.html", {"result": result})


def xyz_there(request: HttpRequest) -> HttpResponse:
    form = xyz_there_form(request.GET)
    if form.is_valid():
        word = form.cleaned_data["word"]
        if "xyz" in word and ".xyz" not in word:
            answer = True
        else:
            answer = False
        return render(request, "form_3.html", {"result": answer})
    else:
        return render(request, "form_3.html")


def centered_average(request: HttpRequest) -> HttpResponse:
    form = centered_average_form(request.GET)
    if form.is_valid():
        a = form.cleaned_data["a"]
        b = form.cleaned_data["b"]
        c = form.cleaned_data["c"]
        d = form.cleaned_data["d"]
        e = form.cleaned_data["e"]
        f = form.cleaned_data["f"]
        g = form.cleaned_data["f"]
        if f == None and g == None:
            array = [a, b, c, d, e]
        elif f != None:
            array = [a, b, c, d, e, f]
        elif f != None and g != None:
            array = [a, b, c, d, e, f, g]

        for n in array:
            if array[0] == n:
                array.remove(n)
            if array[-1] == n:
                array.remove(n)

        almost_done = sum(array)
        answer = almost_done / len(array)
        result = math.floor(answer)
        return render(request, "form_4.html", {"result": result})
    else:
        return render(request, "form_4.html")
