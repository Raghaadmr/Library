from django.shortcuts import render, redirect
from .models import Library, Book
from .forms import SigninForm, MembershipForm, BookForm
from django.contrib.auth import login, authenticate, logout
from django.http import Http404


def signin(request):
    form = SigninForm()
    if request.method == 'POST':
        form = SigninForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            auth_user = authenticate(username=username, password=password)
            if auth_user is not None:
                login(request,auth_user)
                return redirect('book-list')
    context = {
        "form":form
    }
    return render(request, 'signin.html', context)


def signout(request):
    logout(request)
    return redirect('librarian-login')


def membership(request):

    form =  MembershipForm()
    if request.method == 'POST':
        form =  MembershipForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(user.password)
            user.save()
            return redirect("book-list")
    context = {
        "form":form,
    }
    return render(request, 'membership.html', context)

def add_book(request):
    if request.user.is_anonymous:
        return redirect('signin')
    form = BookForm()
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book-list')
    context = {
        "form":form,
    }
    return render(request, 'add_book.html', context)

def book_list(request):
    books = Book.objects.all()
    query = request.GET.get('q')
    if query:
        books = books.filter(
             Q(name__icontains=query)|
             Q(isbn__icontains=query)|
             Q(genre__icontains=query)
                 ).distinct()
    context = {
        "books":Book.objects.all()
    }
    return render(request, 'book_list.html', context)

def book_detail(request, book_id):
    context = {
        "book": Book.objects.get(id=book_id)
    }
    return render(request, 'book_detail.html', context)
