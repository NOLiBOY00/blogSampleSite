from django import forms

from .models import BlogPost

class Editform(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'text']
        labels = {'text': 'Description'}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
