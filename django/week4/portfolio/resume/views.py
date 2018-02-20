from django.shortcuts import render
from .models import Resume, Education, Experience
# Create your views here.

def home(request):
    '''
    Renders home page from resume templates
    '''
    qsEx=Experience.objects.all()
    qsEdu=Education.objects.all()
    qsResume=Resume.objects.first()
    context={'education':qsEdu, 'experience':qsEx, 'resume':qsResume, 'res':'active'}
    return render(request, 'resume/home.html', context)
