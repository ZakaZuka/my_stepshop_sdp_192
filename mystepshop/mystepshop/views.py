from django.shortcuts import render

def index(request):
    return render(request, 'mystepshop/index.html')

def contacts(request):
    return render(request, 'mystepshop/contact.html')

def abouts(request):
    return render(request, 'mystepshop/about.html')




# /static/mystepshop/
