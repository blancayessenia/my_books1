from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, Category

def home(request):
    books = Book.objects.all()
    categories = Category.objects.all()  
    return render(request, 'books/home.html', {
        'books': books,
        'categories': categories
    })


def detail_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'books/detail_book.html', {'book': book})


# CREATE
def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        image = request.POST.get('image')
        category_id = request.POST.get('category')

        category = None
        if category_id:  # solo si seleccionó algo
            category = get_object_or_404(Category, id=category_id)

        Book.objects.create(
            title=title,
            author=author,
            image=image,
            category=category
        )
        return redirect('home')

    return redirect('home')  


# EDIT
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.image = request.POST.get('image')

        category_id = request.POST.get('category')
        if category_id:  # validar que no esté vacío
            book.category = get_object_or_404(Category, id=category_id)
        else:
            book.category = None

        book.save()
        return redirect('home')

    categories = Category.objects.all()
    return render(request, 'books/edit_book.html', {
        'book': book,
        'categories': categories
    })


# DELETE
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect('home')
