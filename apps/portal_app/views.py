# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib import messages
from models import User
from . import forms
from pytz import utc
import bcrypt

# Create your views here.
def display_forms(req):
    context = {
        'reg_form' : forms.reg_form(),
        'login_form' : None
    }
    return render(req, 'portal_app/login_reg.html', context)

def process_login(req):
    results = req.POST
    no_users = len(User.objects.filter(email=results['email']))

    # Check we have exactly one matching user
    if no_users > 1:
        messages.error(req, 'Database error, please don\'t panic')
        return redirect('/')
    elif no_users == 0:
        messages.error(req, 'Email not found')
        return redirect('/')
    
    # Check the password
    maybe_user = User.objects.get(email=results['email'])
    pw_good = bcrypt.checkpw(results['password'].encode(), maybe_user.password.encode())
    
    if pw_good:
        req.session['logged_id'] = maybe_user.id
        messages.success(req, 'All good bro, you check out.')
        return redirect('/poke/view')
    else:
        messages.error(req, 'That password looks wrong, want to try again champ?')
        return redirect('/')

def process_reg(req):
    results = User.objects.validator(req.POST)
    print_results(results)
    
    # Check for errors in validation
    if bad_results(req, results):
        return redirect('/')
    
    # Check for already existing user
    email_matches = User.objects.filter(email=req.POST['email'])
    if not len(email_matches) == 0:
        messages.error(req, 'We already have an entry with that email, first name of {}'.format(email_matches[0].name))
        return redirect('/')

    # Create and save new user
    new_user = User()
    new_user.name = req.POST['name']
    new_user.fake_name = req.POST['fake_name']
    new_user.email = req.POST['email']
    new_user.birthday = utc.localize(results['birthday'][1])
    # For some reason bcrypt had trouble running in the Model class in a helper funciton
    hashed_pw = bcrypt.hashpw(req.POST['password'].encode(), bcrypt.gensalt())
    new_user.password = hashed_pw
    messages.success(req, 'The golem lives, <a href="/poke/view">poke some stuff!</a>')
    new_user.save()

    #Ray detection
    if req.POST['name'].count("Ray") > 0:
        messages.success(req, 'Ray, we\'ve been expecting you... HAHAHAHA')
        req.session['ray'] = True
    return redirect('/')

def print_results(results):
    print """
    Handy Results Inspector
    """
    for result in results:
        print '--> ', result, results[result]

def bad_results(req, results):
    failed = False
    for result in results:
        if not results[result][0]:
            messages.error(req, 'There was a problem with your {}, {}'.format(result, results[result][1]))
            failed = True
    return failed

def logout(req):
    del req.session['logged_id']
    messages.success(req, 'Leave! While I still allow it')
    return redirect('/')