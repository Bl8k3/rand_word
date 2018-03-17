# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import random
from django.shortcuts import render,redirect
def index(request):

    
    return render(request,'index.html')

def randomword(request):
    if 'counter' in request.session:
        request.session['counter']+=1
    else: 
        request.session['counter']=1
    word=''
    my_letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','q','w','x','y','z']
    for times in range(0,26):
        word=word+str(random.choice(my_letters))
    word={
        'random_word':word
    }
    return render('ranomword/index.html',word)
        
def reset(request):
    request.session.clear()
    return redirect('/')
# Create your views here.
