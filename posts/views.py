from django.shortcuts import render
 
from django.shortcuts import get_object_or_404

from django.core.paginator import Paginator

from .models import Post
 
def posts_list(request):
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

    context = {
        'page_object': page,
        'is_paginated': is_paginated,
        'next_url': next_url,
        'previous_url': previous_url
    }

    return render(request, 'posts/home.html', context)

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'posts/detail.html', {'post': post})

    
    