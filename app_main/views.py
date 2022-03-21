from unicodedata import name
from django.shortcuts import render, redirect
from .forms import ImageForm,ContactForm,BuisinessForm
from .models import *

def createpost(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = ImageForm()
    return render(request, 'create_post.html', {'form': form})


def createcontact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, request.GET)
        if form.is_valid():
            form.save()
            return redirect('contacts')
    form = ContactForm()
    return render(request, 'create_contact.html', {'form': form})


def contacts(request):
    contacts = Contact.objects.all()
    title = Contact.objects.all()
    description = Contact.objects.all()
    context = {
        'contacts'         : contacts,
        'title'         : title,
        'description'  : description,

    }
    return render(request,'contacts.html', context)


def posts(request):
    posts = Post.objects.all()
    title = Post.objects.all()
    description = Post.objects.all()
    context = {
        'posts'         : posts,
        'title'         : title,
        'description'  : description,

    }
    return render(request,'posts.html', context)




def createbuisiness(request):
    if request.method == 'POST':
        form = BuisinessForm(request.POST, request.GET)
        if form.is_valid():
            form.save()
            return redirect('buisiness')
    form = BuisinessForm()
    return render(request, 'create_buisiness.html', {'form': form})



def buisiness(request):
    buisiness = Business.objects.all()
    name = Business.objects.all()
    description = Business.objects.all()
    context = {
        'buisiness'    : buisiness,
        'name'         : name,
        'description'  : description,

    }
    return render(request,'buisiness.html', context)


def addalert(request):
    return render(request,'addalert.html')


def alerts(request):
    return render(request,'alerts.html')




