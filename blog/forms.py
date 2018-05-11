from django import forms 
from .models import post

class Text(forms.Form):
	Name = forms.CharField(label='name',max_length=100)

class postForm(forms.ModelForm):
    class Meta:
    	model = post
    	fields=['title','text']

# new code
# new code  2
