from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Project
from django import forms


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description']

        
@login_required
def projects(request):
    projects = Project.objects.filter(created_by=request.user)
    return render(request, 'project/projects.html', {'projects': projects})

@login_required
def project(request, pk):
    projects = Project.objects.filter(created_by=request.user).get(pk=pk)
    return render(request, 'project/projects.html', {'project': project})

@login_required
def add_project(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        description = request.POST.get('description', '').strip()

        if name:
            Project.objects.create(
                name=name,
                description=description,
                created_by=request.user
            )
            messages.success(request, 'Project added successfully!')
            return redirect('project:projects')  # Use named URL
        else:
            messages.error(request, 'Project name is required.')
    
    return render(request, 'project/add.html')