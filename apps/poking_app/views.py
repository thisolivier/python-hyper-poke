# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib import messages
from ..portal_app.models import User, Pokes

# Create your views here.
def show_all(req):
    try:
        int(req.session['logged_id'])
    except:
        messages.success(req, 'You must pass the bouncer before entering the dome.')
        return redirect('/')
    context = {
        'all_users' : User.objects.all().exclude(id=req.session['logged_id']),
        'this_user' : User.objects.get(id=req.session['logged_id'])
    }
    context['poked_by'] = context['this_user'].poked_by
    context['poked_by_no'] = context['poked_by'].count()
    context['evil_peeps'] = get_attackers(req)
    context['fake_query'] = get_totals(req, context['this_user'])
    return render(req, 'poking_app/dashboard.html', context)

def get_attackers(req):
    #Get list of who poked me and how many times
    evil_doers = []
    poked_me = Pokes.objects.filter(victim_id = req.session['logged_id']).order_by('count')
    for poker in poked_me:
        # we have the id of who poked me and the number of times they did
        # we must store their name, and count
        attacker_id = poker.poker_id
        evil_doer = {
            'name' : User.objects.get(id=attacker_id).name,
            'count' : poker.count
        }
        evil_doers.append(evil_doer)
    return evil_doers

def get_totals(req, my_user):
    custom_query = []
    users = User.objects.all().exclude(id=req.session['logged_id'])
    for user in users:
        user_data = {}
        user_data['name'] = user.name
        user_data['email'] = user.email
        user_data['fake_name'] = user.fake_name
        user_data['user_id'] = user.id
        user_data['count'] = 0
        maybe_pokes = Pokes.objects.filter(poker_id = req.session['logged_id'], victim_id = user.id)
        if len(maybe_pokes) > 0:
            user_data['count'] = maybe_pokes[0].count
        print user_data['count']
        custom_query.append(user_data)
    return custom_query

def do_poke(req, victim_id):
    user = User.objects.get(id=req.session['logged_id'])
    victim = User.objects.get(id=victim_id)

    #check if poke exists
    existing_poke = Pokes.objects.filter(poker_id = req.session['logged_id'], victim_id = victim_id)
    if len(existing_poke) == 0:
        print "never happened before"
        poke = Pokes()
        poke.poker = user
        poke.victim = victim
        poke.count = 1
        poke.save()
    else:
        existing_poke[0].count = existing_poke[0].count + 1
        existing_poke[0].save()
        print "------->", existing_poke[0].count
    return redirect('/poke/view')