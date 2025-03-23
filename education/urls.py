from django.urls import path
from . import views

urlpatterns = [
    path('skills/',views.skills,name='skill'),
    path('certifications/',views.certificates,name='certificates'),
    path('projects/',views.projects,name='projects')
]
