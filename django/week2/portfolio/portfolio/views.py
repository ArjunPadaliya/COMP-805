from django.shortcuts import render

def home(request):
    '''
    Returns home page
    '''
    context={'home':'active'}
    return render(request, 'home.html', context)
