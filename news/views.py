from django.http import HttpResponse,Http404
from django.shortcuts import render,redirect
import datetime as dt
#create your views here 

def welcome(request):
    return render(request,'welcome.html')
def news_of_day(request):

    date=dt.date.today()
    #FUNCTION TO CONVERT DATE OBJECT TO FIND EXACT DAY
    
    
    
    return HttpResponse(html)

def past_days_news(request,past_date):

    #this function converts from the strinf url

    try:
        date=dt.datetime.strptime(past_date,'%Y-%m-%d').date()

    except ValueError:
        raise Http404()
        assert False
    if date == dt.date.today():
        return redirect(news_today)

    return render(request,'all-news/past-news.html',{"date":date})

def news_today(request):
    date=dt.date.today()
    return render(request,'all-news/today-news.html',{"date":date})