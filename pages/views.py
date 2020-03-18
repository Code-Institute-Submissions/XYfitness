from django.shortcuts import render, redirect
from .forms import EmailContactForm
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages


# Create your views here.
def home_page(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def contact(request):
    if request.method == 'GET':
        form = EmailContactForm()
    else:
        form = EmailContactForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            send_mail(title, message, email, ['admin@hotmail.com'])
            messages.success(request, "Successfully sent mail")
            return redirect('home')
    return render(request, "contact.html", {'form': form})
