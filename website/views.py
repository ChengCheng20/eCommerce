from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def about(request):
    return render(request, 'about.html', {})

def contact(request):
    return render(request, 'contact.html', {})

def glasses(request):
    return render(request, 'glasses.html', {})

def shop(request):
    return render(request, 'shop.html', {})