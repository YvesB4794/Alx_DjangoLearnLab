from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Post, Comment, Tag


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "email"]

class PostForm(forms.ModelForm):
    # tags input as comma-separated string (optional)
    tags = forms.CharField(required=False, label='Tags (comma separated)',
                           widget=forms.TextInput(attrs={'placeholder': 'python, django, tips'}))

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Post title'}),
            'content': forms.Textarea(attrs={'rows': 10}),
        }

    def clean_tags(self):
        raw = self.cleaned_data.get('tags', '')
        # Normalize: split by comma, strip whitespace, remove empties, unique
        tag_names = [t.strip() for t in raw.split(',') if t.strip()]
        # optionally validate tag name length
        for name in tag_names:
            if len(name) > 50:
                raise forms.ValidationError('Each tag must be 50 characters or fewer.')
        # return normalized list
        return list(dict.fromkeys(tag_names))  # keep order but unique

class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'rows':3}), label='')

    class Meta:
        model = Comment
        fields = ['content']

    def clean_content(self):
        content = self.cleaned_data.get('content', '').strip()
        if not content:
            raise forms.ValidationError("Comment cannot be empty.")
        if len(content) > 2000:
            raise forms.ValidationError("Comment too long (max 2000 characters).")
        return content
    


class PostForm(forms.ModelForm):
    # tags input as comma-separated string (optional)
    tags = forms.CharField(required=False, label='Tags (comma separated)',
                           widget=forms.TextInput(attrs={'placeholder': 'python, django, tips'}))

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Post title'}),
            'content': forms.Textarea(attrs={'rows': 10}),
        }

    def clean_tags(self):
        raw = self.cleaned_data.get('tags', '')
        # Normalize: split by comma, strip whitespace, remove empties, unique
        tag_names = [t.strip() for t in raw.split(',') if t.strip()]
        # optionally validate tag name length
        for name in tag_names:
            if len(name) > 50:
                raise forms.ValidationError('Each tag must be 50 characters or fewer.')
        # return normalized list
        return list(dict.fromkeys(tag_names))  # keep order but unique
