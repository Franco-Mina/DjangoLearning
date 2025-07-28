from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render

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

def monthly_challenge_by_number(request, month):
    try:
        redirect_month = list(monthly_challenges.keys())[month-1]
        return HttpResponseRedirect("/challenges/" + redirect_month)
    except:
        return HttpResponseNotFound("This month is not supported")


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not supported")
