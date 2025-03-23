from django.shortcuts import render

# Create your views here.
def skills(request):
    context={'skill':'active'}
    return render(request,'education/skills.html',context)

def certificates(request):
    context={'certificates':'active'}
    return render(request,'education/certificates.html',context)

def projects(request):
    context = {'projects':'active'}
    return render(request,'education/projects.html',context)