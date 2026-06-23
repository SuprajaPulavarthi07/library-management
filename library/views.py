from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm


from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
@login_required(login_url='/login/')
def home(request):

    books = Book.objects.filter(quantity__gt=0)

    search = request.GET.get('search')
    category = request.GET.get('category')

    if search:
        books = books.filter(title__icontains=search)
        request.session['search'] = search

    if category:
        books = books.filter(category=category)

    last_search = request.session.get('search','')

    return render(request,
                  'home.html',
                  {
                      'books': books,
                      'last_search': last_search
                  })


from django.http import HttpResponse

def user_logout(request):
    logout(request)
    return redirect('/login/')

def add_book(request):

    if not request.user.is_staff:
        return HttpResponse(
            "Access Denied. Only Librarians can add books."
        )

    if request.method == "POST":
        form = BookForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/')

    else:
        form = BookForm()

    return render(
        request,
        'add_book.html',
        {'form': form}
    )

def register(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')

    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})

def set_theme(request):
    response = HttpResponse("Theme saved successfully!")
    response.set_cookie('theme', 'dark')
    return response

def student_login(request):

    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('/')

        else:
            return render(
                request,
                'login.html',
                {'error': 'Invalid Credentials'}
            )

    return render(request, 'login.html')

@login_required(login_url='/login/')
def dashboard(request):

    total_books = Book.objects.count()

    available_books = Book.objects.filter(
        quantity__gt=0
    ).count()

    total_users = User.objects.count()

    books = Book.objects.all()

    return render(
        request,
        'dashboard.html',
        {
            'total_books': total_books,
            'available_books': available_books,
            'total_users': total_users,
            'books': books
        }
    )
