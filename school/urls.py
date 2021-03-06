from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns


urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', include('teachers.urls')),
    path('', include('posts.urls')),
    path('', include('main.urls')),
    path('', include('branches.urls')),
    path('', include('forms.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns  += i18n_patterns(
#     path('', include('teachers.urls')),
#     path('', include('posts.urls')),
#  ) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'main.views.handle_not_found'

