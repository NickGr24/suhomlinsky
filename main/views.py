from django.shortcuts import render


from django.utils import translation
from django.shortcuts import redirect
from django.conf import settings
from django.http import HttpResponseRedirect
from posts.models import Post


def contacts_page(request):
    return render(request, 'contacts.html')


def set_lang(request):
    language = request.POST.get('language', settings.LANGUAGE_CODE)
    translation.activate(language)
    request.session[translation.LANGUAGE_SESSION_KEY] = language
    return HttpResponseRedirect('')
    
def homepage(request):

    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'home.html')
