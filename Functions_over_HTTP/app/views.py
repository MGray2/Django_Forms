from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from app.forms import hey_you_form, age_in_form, order_total_form

# Create your views here.


def order_total(
    request: HttpRequest, burgers: int, fries: int, drinks: int
) -> HttpResponse:
    burger_total = burgers * 4.5
    fries_total = fries * 1.5
    drinks_total = drinks * 1
    ultimate_total = burger_total + fries_total + drinks_total
    return HttpResponse(f"{ultimate_total :.1f}")


def landing_page(request: HttpRequest) -> HttpResponse:
    return render(request, "landing_page.html")


def form_page1(request: HttpRequest) -> HttpResponse:
    form = hey_you_form(request.GET)
    if form.is_valid():
        name = form.cleaned_data["user_name"]
        phrase = f"Hey, {name}!"
        return render(request, "form.html", {"phrase": phrase})
    else:
        phrase = ""
        return render(
            request,
            "form.html",
        )


def form_page2(request: HttpRequest) -> HttpResponse:
    form = age_in_form(request.GET)
    if form.is_valid():
        user_age = form.cleaned_data["user_age"]
        end_year = form.cleaned_data["end_year"]
        new_age = int(end_year) - int(user_age)

    else:
        new_age = ""
    return render(request, "form_2.html", {"new_age": new_age})


def form_page3(request: HttpRequest) -> HttpResponse:
    form = order_total_form(request.GET)
    if form.is_valid():
        burgers = form.cleaned_data["burgers"]
        fries = form.cleaned_data["fries"]
        drinks = form.cleaned_data["drinks"]
        burger_total = burgers * 4.5
        fries_total = fries * 1.5
        drinks_total = drinks * 1
        grand_total = burger_total + fries_total + drinks_total
    else:
        grand_total = ""
    return render(request, "form_3.html", {"total": grand_total})
