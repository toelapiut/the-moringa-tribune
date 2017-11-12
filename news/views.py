from django.http import HttpResponse,Http404
from django.shortcuts import render
import datetime as dt
#create your views here 

def welcome(request):
    return render(request,'welcome.html')
def news_of_day(request):

    date=dt.date.today()
    #FUNCTION TO CONVERT DATE OBJECT TO FIND EXACT DAY
    day=convert_dates(date)
    
    html=f'''
    
        <html>
            <body>
                <h1>News for {day}  {date.day}-{date.month}-{date.year}</h1>
            </body>
        </html>
        '''
    return HttpResponse(html)

def convert_dates(dates):

    #function that gets the weekdays number for the date
    day_number=dt.date.weekday(dates)
    
    days=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

    #Returnin the actual day of the week
    day=days[day_number]
    return day

def past_days_news(request,past_date):

    #this function converts from the strinf url

    try:
        date=dt.datetime.strptime(past_date,'%Y-%m-%d').date()
        day=convert_dates(date)


    
        html=f'''
            <html>
                <body>
                    <h1>News for {day} {date.day}-{date.month}-{date.year}</h1>
                </body>
            </html>
            '''
    except ValueError:
        raise Http404()

    return HttpResponse(html)