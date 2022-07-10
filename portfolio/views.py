from django.shortcuts import render

def index_view(request):
    return render(request, 'index.html')

def test_view(request):
    return render(request, 'test.html')

def contact_view(request):
    return render(request, 'contact.html')

def base_view(request):
    return render(request, 'base.html')
