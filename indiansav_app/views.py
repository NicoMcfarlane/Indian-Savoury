from django.http import HttpRequest
from django.shortcuts import render, redirect, HttpResponseRedirect

from .models import review, indiansav_contact

# Create your views here.


def index(request):
    return render(request, "index.html")

def contact(request):
    if request.method == 'POST':
        row = indiansav_contact(name=request.POST['Name'], message=request.POST['Message'], email=request.POST['Email'], phone=request.POST['Phone'])
        row.save()
        print("Inside Post")
        return HttpResponseRedirect("/contact-us")

    return render(request, "contact.html")

def reviews(request):
    rows = review.objects.all()
    context = {'ratings_list': rows}
    if request.method == 'POST':
        name=request.POST['name']
        email=request.POST['email']
        message=request.POST['message']
        ratings=request.POST['ratings']
        print(name)
        print(email)
        row = review(email= email, message=message, name=name, ratings=ratings)
        row.save()
        print("Inside Post")
        return HttpResponseRedirect("/reviews")

    return render(request, "reviews.html", context)
