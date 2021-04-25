# sendemail/views.py
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from .models import ContactForm
from .forms import UserModelForm


def validateEmail( email ):
    try:
        validate_email(email)
        return True
    except ValidationError:
        return False

def repeatedCorrectly(email1,email2):
    print(email1,email2)
    try:
        if (email1 == email2):
            return True
    except ValidationError:
        return False
            
def contactView(request):
    if request.method == 'GET':
        form = ContactForm()
    elif request.method == 'POST':
        form = UserModelForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            validateEmail(from_email)
            repeat_email = form.cleaned_data['repeat_email']
            validateEmail(repeat_email)
            print(repeatedCorrectly(from_email,repeat_email))
            message = form.cleaned_data['message']
            u = form.save()
            print({'form': form})


            
            try:
                send_mail(subject, message, from_email, ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    else:
        form_class = UserModelForm
    return render(request, "email.html", {'form': form})

def successView(request):
    return HttpResponse('Success! Thank you for your message.')