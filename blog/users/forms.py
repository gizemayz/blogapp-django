from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from blogapp.models import Post, Comment, Category
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'image', 'category', 'content']


class UpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'image', 'category', 'content']


class DeleteForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'body']


class CatForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
