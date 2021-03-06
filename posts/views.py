from django.shortcuts import render
 
from django.shortcuts import get_object_or_404

from django.core.paginator import Paginator

from django.db.models import Q

from .models import Post, PostImage
 
def posts_list(request):

    search_query = request.GET.get('search', '')
    if search_query and search_query != '':
        posts = Post.objects.filter(Q(title__icontains=search_query) | Q(text__icontains=search_query))
    else:
        posts = Post.objects.all()
    paginator = Paginator(posts, 7)

    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    is_paginated = page.has_other_pages()
    
    if page.has_previous():
        previous_url = '?page={}'.format(page.previous_page_number())
    else:
        previous_url = ''

    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''
    photos = PostImage.objects.all()
    context = {
        'page_object': page,
        'is_paginated': is_paginated,
        'next_url': next_url,
        'previous_url': previous_url,
        'photos': photos,
        
    }

    return render(request, 'posts/home.html', context)

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    photos = PostImage.objects.filter(post=post)
    return render(request, 'posts/detail.html', {'post': post, 'photos': photos})

    
    