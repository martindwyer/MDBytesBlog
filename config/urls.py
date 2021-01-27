"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from datetime import datetime
from django.conf.urls import url
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact_view, name='contact'),
    path('about/', views.about, name='about'),
    path('posts/', views.PostListView.as_view(), name='post_list'),
    url(r'post/(?P<pk>\d+)$', views.PostDetailView.as_view(),
        name='post_detail'),
    path('post/new/', views.CreatePostView.as_view(), name='post_new'),
    url(r'post/(?P<pk>\d+)/edit$', views.PostUpdateView.as_view(),
        name='post_edit'),
    url(r'post/(?P<pk>\d+)/remove$', views.PostDeleteView.as_view(),
        name='post_remove'),
    url(r'post/(?P<pk>\d+)/publish$', views.post_publish,
        name='post_publish'),
    url(r'^comment/(?P<pk>\d+)/approve/$', views.comments_approve,
        name='comment_approve'),
    url(r'drafts/$',
        views.DraftListView.as_view(template_name='app/draft_list.html'),
        name='post_draft_list'),
    path('post/<pk>/comment/', views.add_comment_to_post,
         name='add_comment_to_post'),
    url(r'^comment/(?P<pk>\d+)/approve/$', views.comments_approve,
        name='comment_approve'),
    url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove,
        name='comment_remove'),
    path('login/',
         LoginView.as_view
             (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year': datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
]
