from django.shortcuts import render
from BookAdminApp.models import Category,Book

# Create your views here.
def home(request):
    cats = Category.objects.all()
    books = Book.objects.all()
    return render(request,"master.html",{"cats":cats,"books":books})

def ShowBooks(request,id):
    cats = Category.objects.all()
    books = Book.objects.filter(category = id)
    return render(request,"master.html",{"cats":cats,"books":books})

def ViewDetails(request,id):
    cats = Category.objects.all()
    book = Book.objects.get(id = id)
    return render(request,"master.html",{"cats":cats,"book":book})