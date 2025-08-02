from django.urls import reverse
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

monthly_challenges = {
    "january": "This is the challenge for january!",
    "february": "This is the challenge for february!",
    "march": "This is the challenge for march!",
    "april": "This is the challenge for april!",
    "may": "This is the challenge for may!",
    "june": "This is the challenge for june!",
    "july": "This is the challenge for july!",
    "august": "This is the challenge for august!",
    "september": "This is the challenge for september!",
    "october": "This is the challenge for october!",
    "november": "This is the challenge for november!",
    "december": "This is the challenge for december!",
}

# Create your views here.

def monthly_challenge_list(request):
    month_list = monthly_challenges.keys()
    text_list ="<ul>"
    for month in month_list:
        text_list += f"<li><a href={reverse("month-challenge", args=[month])}>{month}</a></li>"
    text_list += "</ul>"
    return HttpResponse(text_list)

def monthly_challenge_by_number(request, month):
    try:
        redirect_month = list(monthly_challenges.keys())[month-1]
        redirect_path = reverse("month-challenge", args=[redirect_month])
        return HttpResponseRedirect(redirect_path)
    except:
        return HttpResponseNotFound("This month is not supported.")


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>This month is not supported.</h1>")
