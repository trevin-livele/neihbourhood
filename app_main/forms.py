from django import forms
from .models import Post,Contact,NeighbourHood,Business





class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Post
        fields = ('title', 'image','description','category')



class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name','email','phone','neighbourhood']


class BuisinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ['name','email','description']





    