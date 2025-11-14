from django import forms
from .models import Book

class ExampleForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author']

class BookSearchForm(forms.Form):
    query = forms.CharField(
        max_length=255,
        required=False,
        widget=forms.TextInput(attrs={"placeholder": "Search for a book"})
    )
