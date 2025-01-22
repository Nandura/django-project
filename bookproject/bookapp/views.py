from django.shortcuts import render, redirect
from django.template.defaultfilters import title

from . models import Book

# Create your views here.

def createbook(request):
    

    if request.method =='POST':
        title = request.POST.get('title')
        price = request.POST.get('price')

        book = Book(title=title,price=price)

        book.save()
    return render(request,'book.html')

def list(request):
    books = Book.objects.all()
    return render(request,'listview.html',{'books':books})

def viewlist(request,book_id):
    book = Book.objects.get(id=book_id)
    return  render(request,'views.html',{'book':book})

def updatebook(request,book_id):
    book = Book.objects.get(id=book_id)
    if request.method =='POST':
        title = request.POST.get('title')
        price = request.POST.get('price')
        book.title = title
        book.price = price


        book.save()
        return redirect('/')
    return render(request,'update.html',{'book':book})

def delect(request,book_id):
    book = Book.objects.get(id=book_id)

    if request.method == 'POST':

        book.delete()
        return redirect('/')

    return  render(request,'detel.html',{'book':book})