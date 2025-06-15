from django.shortcuts import render, redirect
from django.db.models import Q

from .models import Project


def home(request):
    projects = Project.objects.all()
    return render(request, 'index.html', context={'projects': projects})


def advanceSearch(request):
    language = request.POST.get('language')
    field = request.POST.get('field')
    query = request.POST.get('query')

    if request.method == 'POST':
        projects = projectByLanguage(language) & projectByField(field) & projectBySkills(query)
        return render(request, 'index.html', context={'aq': True, 'projects': projects})

    projects = Project.objects.all()
    return render(request, 'index.html', context={'aq': True, 'projects': projects})


def project(request, id):
    project = Project.objects.get(id=id)
    return render(request, 'project.html', context={'project': project})


def projectByField(field):
    return Project.objects.filter(Q(field__icontains=field))


def projectByLanguage(language):
    return Project.objects.filter(Q(language__icontains=language))


def projectBySkills(skills):
    return Project.objects.filter(Q(skills__icontains=skills))
