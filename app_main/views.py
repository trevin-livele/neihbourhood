from django.shortcuts import render, redirect
from .forms import ImageForm,ContactForm,BuisinessForm
from .models import *
from django.contrib.auth.decorators import login_required

@login_required(login_url = 'login')
def createpost(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = ImageForm()
    return render(request, 'create_post.html', {'form': form})

@login_required(login_url = 'login')
def createcontact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, request.GET)
        if form.is_valid():
            form.save()
            return redirect('contacts')
    form = ContactForm()
    return render(request, 'create_contact.html', {'form': form})

@login_required(login_url = 'login')
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

@login_required(login_url = 'login')
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



@login_required(login_url = 'login')
def createbuisiness(request):
    if request.method == 'POST':
        form = BuisinessForm(request.POST, request.GET)
        if form.is_valid():
            form.save()
            return redirect('buisiness')
    form = BuisinessForm()
    return render(request, 'create_buisiness.html', {'form': form})


@login_required(login_url = 'login')
def buisiness(request):
    buisiness = Business.objects.all()
    name = Business.objects.all()
    email = Business.objects.all()
    description = Business.objects.all()
    phone      = Business.objects.all()
    user       = Business.objects.all()
    location   = Business.objects.all()

    context = {
        'buisiness'    : buisiness,
        'name'         : name,
        'description'  : description,
        'name'       : name,         
        'email'      :  email,
        'phone'       :  phone,
        'user'        :   user,
        'location'     : location,
}


    return render(request,'buisiness.html', context)

@login_required(login_url = 'login')
def addalert(request):
    return render(request,'addalert.html')

@login_required(login_url = 'login')
def alerts(request):
    return render(request,'alerts.html')




