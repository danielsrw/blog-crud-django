from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.allposts, name = 'allposts'),
    path('post/<slug>/', views.post, name = 'post'),
    path('about/', views.about,name = 'about' ),
    path('search/', views.search, name = 'search'),
    path('postlist/<slug>/', views.postlist, name = 'postlist'), 
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)