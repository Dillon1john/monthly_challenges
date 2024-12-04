from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from flask import request
from django.template.loader import render_to_string


monthly_challenges = {
    'january': 'Eat no meat for the entire month!',
    'february': 'Walk for at least 20 minutes every day!',
    'march': 'Learn Django for at least 20 minutes every day!',
    'april': 'Eat no meat for the entire month!',
    'may': 'Walk for at least 20 minutes every day!',
    'june': 'Learn Django for at least 20 minutes every day!',
    'july': 'Eat no meat for the entire month!',
    'august': 'Walk for at least 20 minutes every day!',
    'september': 'Learn Django for at least 20 minutes every day!',
    'october': 'Eat no meat for the entire month!',
    'november': 'Walk for at least 20 minutes every day!',
    'december': None
}
# Create your views here.

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())
    return render(request, 'challenges/index.html', {'months': months})
    

def monthly_challenge_by_number(request, month):
    try:
        months = list(monthly_challenges.keys())
        redirect_month = months[month - 1]
        redirect_path = reverse('month-challenge', args=[redirect_month]) #/challenge/january
        return HttpResponseRedirect(redirect_path)
    except:
        return HttpResponseNotFound('This month is not supported!')
    
    
def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request,'challenges/challenge.html',{'text':challenge_text , 'month': month.capitalize()})
    except:
       raise Http404()