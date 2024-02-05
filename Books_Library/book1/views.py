from django.shortcuts import render, HttpResponse, redirect
from .models import Book
from django.db.models import Q

# Create your views here.


def index_page(request):
    return render(request, 'index.html')


def show_books(request):
    books = Book.objects.all()
    context = {
        'books' : books
    }
    return render(request, 'show_books.html', context)


def add_books(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        quantity = request.POST.get('quantity')
        price = request.POST.get('price')
        author = request.POST.get('author')
        published_date = request.POST.get('published_date')
        new_book = Book(name=name, quantity=quantity, price=price, author=author, published_date=published_date)
        new_book.save()
        return redirect("add_books")
    elif request.method== 'GET':
        return render(request, 'add_book.html')
    else:
        return HttpResponse("Error Occured")
    



def update_book(request):
    if request.method == 'POST':
        # Get the values from the form
        book_id = request.POST.get('book_id')
        name = request.POST.get('name')
        quantity = request.POST.get('quantity')
        price = request.POST.get('price')

        try:
            # Retrieve the book to be updated
            book_to_be_updated = Book.objects.get(id=book_id)

            # Update the book fields
            if name:
                book_to_be_updated.name = name

            if quantity:
                book_to_be_updated.quantity = quantity

            if price:
                book_to_be_updated.price = price

            # Save the updated book
            book_to_be_updated.save()

            # Redirect to a success page or render updated books
            # For now, redirect to the show_books page
            return redirect('show_books')

        except Book.DoesNotExist:
            return HttpResponse("Please enter a valid book ID")

    elif request.method == 'GET':
        # Render the form
        return render(request, 'update_book.html')

    else:
        return HttpResponse("An error occurred")
    



def delete_book(request, pk=None):
    if pk:
        try:
            book_to_be_deleted = Book.objects.get(id=pk)
            book_to_be_deleted.delete()
            return redirect('delete_book')
        except:
            return("plz enter valid id")
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'delete_book.html', context)




