from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import BlogPost
from .forms import Editform

# Create your views here.

def index(request):
    """The index view"""
    return render(request, 'blogs/index.html')

@login_required
def view_all(request):
    """View all blog post"""
    blogpost = BlogPost.objects.filter(owner=request.user).order_by('-date_added')

    content = {'blog_post': blogpost}
    return render(request, 'blogs/view_all.html', content)

@login_required
def edit_blog(request, blog_id):
    """View to edit blog post"""
    edit = BlogPost.objects.get(id=blog_id)

    # Check for the user
    check_blog_owner(edit, request)

    if request.method != 'POST':
        form = Editform(instance=edit)
    else:
        # Post data submitted
        form = Editform(instance=edit, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:view_all')
    
    context = {'title': edit.title, 'text': edit.text,
               'blog_id': edit.id , 'form': form}
    return render(request, 'blogs/edit_blog.html', context)

@login_required
def view_post(reuquest, blog_id):
    """View a specific post"""
    blogpost = BlogPost.objects.get(id=blog_id)

    # Check for the user
    check_blog_owner(blogpost, reuquest)

    content = {'title': blogpost.title, 'text': blogpost.text, 
               'date_': blogpost.date_added}
    return render(reuquest, 'blogs/view_post.html', content)

@login_required
def new_post(request):
    """Add new post"""
    if request.method != 'POST':
        # Create  blank form
        form = Editform()
    else:
        # Post data submitted.
        form = Editform(data=request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.owner = request.user
            new_post.save()
            return redirect('blogs:view_all')

    # Display a blank form
    context = {'form': form}
    return render(request, 'blogs/new_post.html', context)

@login_required
def titleView(request):
    posts = BlogPost.objects.filter(owner=request.user).order_by('date_added')

    context = {'posts': posts}
    return render(request,'blogs/titleView.html', context)

def check_blog_owner(blog, request):
    if blog.owner != request.user:
        raise Http404