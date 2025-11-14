# bookshelf/forms.py
from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author']

class BookSearchForm(forms.Form):
    q = forms.CharField(required=False, max_length=200)

    def clean_q(self):
        q = self.cleaned_data.get('q', '')
        # strip control characters, limit length — more rules as needed
        return q.strip()
