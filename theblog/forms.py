from django import forms
from django.forms import fields
from django.forms.widgets import Select
from .models import Category, Comment, Post

class UserPost(forms.ModelForm):
    status = forms.ChoiceField(choices=Post.STATUS)
    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label='Select')
    class Meta:
        model = Post
        fields = ['title', 'title_tag', 'body', 'image', 'category', 'status']

        widgets = {
            'title' : forms.TextInput(attrs={'placeholder' : 'This is title'}),
            'title_tag' : forms.TextInput(attrs={'placeholder' : 'This is title-tag'}),
            'body' : forms.Textarea(attrs={'placeholder' : 'This is content'}),
            # 'category' : forms.Select(attrs={'placeholder' : 'This is content'}),
            # 'status' : forms.Select(attrs={'placeholder' : 'This is content'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content',]