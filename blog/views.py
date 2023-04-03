from django.shortcuts import render
from .models import post
from django.views import generic

# Create your views here.

class BlogView(generic.DetailView):
    model = post
    template_name = 'blog.html'

class AboutView(generic.TemplateView):
    template_name = 'about.html'

class post_list(generic.ListView):
    queryset = post.objects.filter(status=1).order_by('-date_created')
    template_name = 'index.html'
