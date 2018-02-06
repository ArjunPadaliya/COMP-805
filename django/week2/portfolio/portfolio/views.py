from django.shortcuts import render

def home(request):
    '''
    Returns home page
    '''
    context={'home':'active'}
    return render(request, 'home.html', context)

def resume(request):
    '''
    Returns resume page
    '''
    context={'resume':'active'}
    return render(request, 'resume.html', context)

def portfolio(request):
    '''
    Returns resume page
    '''
    context={'portfolio':'active'}
    return render(request, 'portfolio.html', context)

def contact(request):
    '''
    Returns contact page
    '''
    context={'contact':'active'}
    return render(request, 'contact.html', context)
