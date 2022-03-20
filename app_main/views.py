from django.shortcuts import render, redirect
from .forms import ImageForm,ContactForm
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
            return redirect('home')
    form = ContactForm()
    return render(request, 'create_contact.html', {'form': form})


def contacts(request):
    contacts = Contact.objects.all()
    title = Post.objects.all()
    description = Post.objects.all()
    context = {
        'contacts'         : contacts,
        'title'         : title,
        'description'  : description,

    }
    return render(request,'contacts.html', context)
