from django import forms
from .models import Post,Contact,NeighbourHood





class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Post
        fields = ('title', 'image','description')



class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name','email','phone','neighbourhood']





    