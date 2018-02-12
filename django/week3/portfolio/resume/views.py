from django.shortcuts import render
from .models import Education, Experience
# Create your views here.

def home(request):
    '''
    Renders home page from resume templates
    '''
    qsEx=Experience.objects.all()
    qsEdu=Education.objects.all()
    context={'experience': qsEx, 'education':qsEdu}
    return render(request, 'resume/home.html', context)
