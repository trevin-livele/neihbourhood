from django.shortcuts import render
from app_main .models import Post

def home(request):
    posts = Post.objects.all()
    title = Post.objects.all()
    description = Post.objects.all()
    context = {
        'posts'         : posts,
        'title'         : title,
        'description'  : description,

    }
    return render(request,'home.html', context)



