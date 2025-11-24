from django import forms
from blogs.models import Post
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'published', 'image']
        
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title)< 5:
            raise forms.ValidationError("title must be at least 5 character long")
        return title 

class UserRegistrationForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    
    def clean(self):
        cleaned_data = super().clean()
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError("Passwords does not match")
        return cleaned_data

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class CommentForm(forms.ModelForm):
    content = forms.CharField( 
        widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'Write your comment here...'}),
    label=''
    )

    class Meta:
        model = Comment
        fields = ['content']
        

