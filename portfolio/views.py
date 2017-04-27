from django.shortcuts import render, HttpResponse
from django.views import generic
from django.views.generic.edit import CreateView
from .models import Project
# Create your views here.
class IndexView(generic.ListView):
    template_name = 'portfolio/index.html'
    context_object_list = 'latest_posts_list'
    
    def get_queryset(self):
        return Project.objects.order_by('-pub_date')[:5]

class CreateProject(CreateView):
    model = Project
    fields = ["project_name", "project_description", "project_source"]
    