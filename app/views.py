from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse

# Create your views here.


# says hello to requested name
def hey_you(request: HttpRequest, you: str) -> HttpResponse:
    return HttpResponse(f"Hey, {you}!")


# tells you your age using a target year and a target birthdate
def age_in(request: HttpRequest, year: int, birth: int) -> HttpResponse:
    new_age = year - birth
    return HttpResponse(new_age)


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
    return render(request, "form.html")


def form_page2(request: HttpRequest) -> HttpResponse:
    return render(request, "form_2.html")


def form_page3(request: HttpRequest) -> HttpResponse:
    return render(request, "form_3.html")
