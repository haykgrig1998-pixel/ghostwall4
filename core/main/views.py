from django.shortcuts import render
import logging
from django.conf import settings
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.core.mail import EmailMessage,send_mail
from django.core.validators import validate_email
from django.shortcuts import render, redirect


def contact_view(request):
    if request.method == 'POST':
        # Ստուգում ենք honeypot-ը (spam-ի դեմ)
        if request.POST.get('website'):
            return redirect('contact')
            
        name = request.POST.get('name')
        email = request.POST.get('email')
        company = request.POST.get('company', '-')
        message = request.POST.get('message')
        
        # Ձևավորում ենք նամակի տեքստը
        subject = f"New Contact Message from {name} ({company})"
        email_body = f"Name: {name}\nEmail: {email}\nCompany: {company}\n\nMessage:\n{message}"
        
        try:
            # Ուղարկում ենք նամակը ձեր Gmail-ին
            send_mail(
                subject,
                email_body,
                settings.EMAIL_HOST_USER,  # Ուղարկող (ձեր Gmail-ը)
                [settings.CONTACT_RECEIVER], # Ստացող (ձեր Gmail-ը)
                fail_silently=False,
            )
            messages.success(request, "Your message has been sent successfully!")
        except Exception as e:
            messages.error(request, f"Error sending message: {e}")
            
        return redirect('contact')
        
    return render(request, 'your_contact_template.html')

def home(request):
    return render(request, 'home.html')


def platform(request):
    return render(request, 'platform.html')


def solutions(request):
    return render(request, 'solutions.html')


def pricing(request):
    return render(request, 'pricing.html')


def contact(request):
    return render(request, 'contact.html')