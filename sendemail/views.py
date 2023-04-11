# sendemail/views.py
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from .models import ContactsModel, UserType
from .forms import ContactsModelForm
from django.contrib.auth.models import User
from .models import UserProfile
from .forms import UserProfileForm
from django.forms.models import inlineformset_factory
from django.core.exceptions import PermissionDenied

from django.urls import reverse
from .forms import CustomUserCreationForm
from django.contrib.auth import login

def validateEmail( email ):
    try:
        validate_email(email)
        return True
    except ValidationError:
        return False

            
def contactView(request):
    if request.method == 'GET':
        form = ContactsModelForm()
        user_type = UserType()
    elif request.method == 'POST':
        form = ContactsModelForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            validateEmail(from_email)
            repeat_email = form.cleaned_data['repeat_email']
            validateEmail(repeat_email)
            message = form.cleaned_data['message']
            u = form.save()
            print({'form': form})

            try:
                send_mail(subject, message, from_email, ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    else:
        form_class = ContactsModelForm
    
    return render(request, "email.html", {'form': form})

def successView(request):
    return HttpResponse('Success! Thank you for your message.')

#Added April 27

def dashboard(request):
    return render(request, "dashboard.html")

def register(request):
    if request.method == "GET":
        return render(
            request, "register.html",
            {"form": CustomUserCreationForm}
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("dashboard"))

def edit_user(request):
    user_id = request.user.id
    request.UserProfile.isteacher
    
    user = User.objects.get(pk=user_id)
    user_form = UserProfileForm(instance=user)

    ProfileInlineFormset = inlineformset_factory(User, UserProfile, fields=('is_teacher', 'bio', 'phone', 'city', 'country', 'organization'))
    formset = ProfileInlineFormset(instance=user)

    #if request.user.is_authenticated() and request.user.id == user.id:
    if request.user.id == user.id:
        if request.method == "POST":
            user_form = UserProfileForm(request.POST, request.FILES, instance=user)
            formset = ProfileInlineFormset(request.POST, request.FILES, instance=user)

            if user_form.is_valid():
                created_user = user_form.save(commit=False)
                formset = ProfileInlineFormset(request.POST, request.FILES, instance=created_user)

                if formset.is_valid():
                    created_user.save()
                    formset.save()
                    return HttpResponse('Success! User updated.')
                    #return HttpResponseRedirect('base.html')

        return render(request, "account_update.html", {
            "noodle": user_id,
            "noodle_form": user_form,
            "formset": formset,
        })
    else:
        raise PermissionDenied