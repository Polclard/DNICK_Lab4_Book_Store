from django.http import HttpResponse
from django.shortcuts import render
from django.template.defaultfilters import register
from .forms import BookForm

from BookStore.models import Book, PublishingHouse, BOOK_CATEGORIES, PAGES_TYPES


# Create your views here.

def index(request):
    books_list = Book.objects.all()

    context = {
        "books_list": books_list
    }

    return HttpResponse(render(request, template_name="index.html", context=context))


def book_detail(request, book_id):
    found_book = Book.objects.filter(id=book_id).first()

    context = {
        "found_book": found_book
    }

    return HttpResponse(render(request, "bookDetails.html", context=context))


def add_book(request):
    if request.method == "POST":
        book = BookForm(request.POST, request.FILES)
        if book.is_valid():
            book.save()
    else:
        book = BookForm()

    return render(request, "addBookForm.html", {"form": book})


@register.filter("modulo")
def modulo(num, val):
    return num % val
