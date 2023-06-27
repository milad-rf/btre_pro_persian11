from tkinter.messagebox import YES
from django.shortcuts import render, redirect

from contacts.admin import ContactAdmin
from .models import contacts
from django.contrib import messages

def contact(request):
    if request.method == 'POST':
       listing_id = request.POST['listing_id']
       listing = request.POST['listing']
       name = request.POST['name']
       email = request.POST['email']
       phone = request.POST['phone']
       message = request.POST['message']
       user_id = request.POST['user_id']
       listing_id = request.POST['listing_id']
       listing_id = request.POST['listing_id']
       realtor_email = request.POST['realtor_email']
       
       contact= ContactAdmin(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone,
       message=message, user_id=user_id)

       contact.save()

       message.success(request, 'Your req has been submitted, a realtr will call you back.')
       return redirect('/listings/'+listing_id)