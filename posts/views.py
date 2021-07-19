from django.shortcuts import render

from django.views.generic import ListView, DetailView
 
from .models import Post
 
class PostsListView(ListView):
    model = Post
    template_name = 'posts/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.all()
        return context

    def  get_queryset(self, *args, **kwargs):
        request = self.request
        return Post.objects.all()
    

class PostsDetailView(DetailView):
    model = Post
    template_name = 'posts/detail.html'

    
    