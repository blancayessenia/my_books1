from django.shortcuts import render, get_object_or_404, redirect
from .models import Book

def home(request):
    books = Book.objects.all()
    return render(request, 'books/home.html', {'books': books})

def detail_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'books/detail_book.html', {'book': book})