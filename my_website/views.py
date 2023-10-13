from django.shortcuts import render,redirect
from django.http import FileResponse
from django.conf import settings
from my_website.models import Contact
from . forms import ContactForm
from django.contrib import messages
import os
from django.core.mail import send_mail


def contact(request):
    
    form = ContactForm()
    message = ""
    context = {"form": form, "message": message}
     
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            
             # Récupérer les données soumises
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
             
             # Envoi de l'e-mail
            send_mail("Nouveau message via ton site internet de",
                       f'Nom: {name}\nTéléphone: {phone}\nEmail: {email}\nMessage: {message}',
                       'djokodev75@gmail.com',
                       ['djokodev75@gmail.com'],
                       fail_silently=False,)
            
            
            
            message = "Votre message a bien été transmis, nous vous contacterons dans moins d'une Heure. Merci 😉✨ "
            
            form = ContactForm() #dois vider le formulaire!

        context = {"form": form, "message":message}
           
    return render(request, "index.html", context=context)


def download(request):
    file = os.path.join(settings.BASE_DIR, 'my_website/static/my_website/assets/img/moncv.pdf')

    fileOpened = open(file, 'rb')

    return FileResponse(fileOpened)


def index(request):
    return render (request, "index.html")



