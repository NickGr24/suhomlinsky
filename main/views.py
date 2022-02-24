from django.shortcuts import render
from posts.models import Post


def contacts_page(request):
    return render(request, 'contacts.html')

def homepage(request):
    return render(request, 'home.html')

def handle_not_found(request, exception):
    return render(request, '404.html', status=404)

def goleni(request):
    return render(request, 'filials/goleni.html')

def sofrincani(request):
    return render(request, 'filials/sofrincani.html')

def constantinovca(request):
    return render(request, 'filials/constantinovca.html')