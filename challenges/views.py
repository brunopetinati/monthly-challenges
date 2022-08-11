from turtle import forward
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

monthly_challenges = {
    'january': 'eat no meat for this month!',
    'february': 'walk 20 minutes every day!',
    'march': 'study django for 20 minutes a day',
    'april': 'go every saturday to a different nightclub',
    'may': 'help one animal per week on the street',
    'june': 'walk with 1 cat a day on the street',
    'july': 'understand how to host a website in a server machine',
    'august': 'just try to survive this month',
    'september': 'try to figure out how to charge credit cards through a web app',
    'october': 'play pump it up every sunday',
    'november': 'finish reading 3 books',
    'december': 'start the technical book in web development'
}

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys()) # ['january','february'...]

    if month > len(months):
        return HttpResponseNotFound('invalid month')

    redirect_month = months[month - 1]
    redirect_path = reverse('path_name', args=[redirect_month]) # /challenge/january

    #return HttpResponseRedirect('/challenges/' + redirect_month)
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    
    try:
        challenge_text = monthly_challenges[month]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound('<h1>this month is not supported</h1>')