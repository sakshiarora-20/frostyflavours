from django.shortcuts import render, redirect, HttpResponse
from datetime import datetime
from myapp.models import Contact
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from myapp.models import Flavour
from django.db.models import Q

@login_required
def index(request):
    flavours = Flavour.objects.all()
    return render(request, "index.html", {'flavours': flavours})

@login_required
def about(request):
    return render(request, "about.html")

@login_required
def services(request):
    return render(request, "services.html")


def signin(request):
    return render(request, "signin.html")


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/home')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, "signin.html")

def logout_view(request):
    logout(request)
    return redirect("/signin")


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        msg = request.POST.get('message')
        date = datetime.today()

        contact = Contact(name=name, email=email, phone=phone, msg=msg, date=date)
        contact.save()
        messages.success(request, "Message sent successfully.")
        
    return render(request, "contact.html")


def search_flavours(request):
    query = request.GET.get('q')
    if query:
        results = Flavour.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )
    else:
        results = Flavour.objects.all()

    return render(request, 'index.html', {'flavours': results, 'query': query})
