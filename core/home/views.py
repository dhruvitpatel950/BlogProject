from django.shortcuts import render
from django.http import HttpResponse

def home(request):

    peoples = [
        {'name': 'Dhruvit','age': 21},
        {'name': 'Dev','age': 22},
        {'name': 'Harsh','age': 25},
        {'name': 'Vatsal','age': 26},
        {'name': 'Sidhharth','age': 24}
    ]

    text = """Lorem ipsum dolor sit amet, consectetur adipisicing elit. Neque culpa odit, aspernatur minus nulla nemo ipsam, quia sint reiciendis fugit aperiam illum reprehenderit repellat totam. Libero eligendi animi ipsam magni?"""
    
    return render(request, "home/index.html", {"peoples": peoples , "text": text, 'page': 'Home'})

def contact(request):
    context = {'page': 'contact'}
    return render(request, "home/contact.html", context)

def about(request):
    context = {'page': 'about'}
    return render(request, "home/about.html", context)

def success_page(request):
    return HttpResponse("<h1>this one is success page </h1>")
