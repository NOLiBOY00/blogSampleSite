"""Defines URL patterns for blogs."""

from django.urls import path

from . import views

app_name = 'blogs'
urlpatterns = [
    # Page for index view
    path('', views.index, name='index'),
    # Page view all the blog post
    path('view_all/', views.view_all, name='view_all'),
    # Page view to edit blog post
    path('edit_blog/<int:blog_id>', views.edit_blog, name='edit_blog'),
    # Page view specific post
    path('view_post/<int:blog_id>', views.view_post, name='view_post'),
    # Page view add a new post
    path('new_post/', views.new_post, name='new_post'),
    # Page view all title
    path('titleView', views.titleView, name='titleView')
]