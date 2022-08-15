from turtle import forward
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

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
    'december': None
}

def index(request):
    months = list(monthly_challenges.keys())

    return render(request, 'challenges/index.html', {
        'months': months # and that's how you provide a list for the template to iterate
    })

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys()) # ['january','february'...]

    if month > len(months):
        return HttpResponseNotFound('invalid month')

    redirect_month = months[month - 1]
    redirect_path = reverse('path_name', args=[redirect_month]) # /challenge/january

    #return HttpResponseRedirect('/challenges/' + redirect_month)
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    
    #try:    
        #pdb.set_trace()
        challenge_text = monthly_challenges[month]
        
        # always takes request as first argument # object with the variables and their values
        return render(request, 'challenges/challenge.html', {
            'month': month, 
            'challenge': challenge_text
        }) 
        # response_data = render_to_string('challenges/challenge.html')
        # return HttpResponse(response_data)
        # due to django.shortcuts it's possible to skip those 2 lines above 
    #except:
    #   return HttpResponseNotFound('<h1>this month is not supported</h1>')