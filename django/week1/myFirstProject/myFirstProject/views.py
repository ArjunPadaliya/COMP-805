from django.shortcuts import render

def home(request):
    '''
    Renders home page
    '''
    greeting="uStudy-the best study site in the world!"
    days_of_week=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    context={'our_greetings': greeting ,'weekday_list':days_of_week}
    return render(request, 'home.html', context)
