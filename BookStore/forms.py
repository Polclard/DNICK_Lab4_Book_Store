from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"
        widgets = {
            'release_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
