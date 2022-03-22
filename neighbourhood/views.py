from unicodedata import category
from django.shortcuts import render
from app_main .models import Contact, Post
from django.contrib.auth.decorators import login_required


@login_required(login_url = 'login')
def home(request):
    posts = Post.objects.all()
    title = Post.objects.all()
    description = Post.objects.all()
    category = Post.objects.all()
    context = {
        'posts'         : posts,
        'title'         : title,
        'description'  : description,
        'category'      : category,

    }
    return render(request,'home.html', context)






