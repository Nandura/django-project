from django.shortcuts import render
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