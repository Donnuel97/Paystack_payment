from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,HttpRequest
from django.conf import settings
from . models import *
from . import forms
from django.contrib import messages
 

from . import forms

def initiate_payment(request) -> HttpResponse:
    if request.method == 'POST':
        payment_form = forms.PaymentForm(request.POST)
        if payment_form.is_valid():
            payment = payment_form.save()
            return render(request, 'make_payment.html',{'payment':payment, 'paystack_public_key':settings.PAYSTACK_PUBLIC_KEY})
    else:
        payment_form = forms.PaymentForm()
    return render(request, 'initiate-payment.html',{'payment_form':payment_form})

def  verify_payment(request:HttpRequest, ref: str) -> HttpResponse:
    payment = get_object_or_404(Payment, ref=ref)
    verified = payment.verify_payment()
    if verified:
        messages.success(request, 'verification successful')
    else:
        messages.error(request,'verification failed')
    return render(request, 'success.html')