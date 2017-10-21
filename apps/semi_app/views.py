from django.shortcuts import render, redirect
from django.contrib import messages
from models import *

# Create your views here.

def index(request):
    context = {
        "users": User.objects.all()
    }
    return render(request, 'semi_app/index.html', context)

def show(request, num):

    context = {
        'id': num,
        'name': User.objects.get(id=num).first_name + " " + User.objects.get(id=num).last_name,
        'email': User.objects.get(id=num).email,
        'created': User.objects.get(id=num).created_at
    }

    return render(request, 'semi_app/user.html', context)

def new(request):

    return render(request, 'semi_app/add_user.html')

def edit(request, num):

    context = {
        "user": User.objects.get(id=num)
    }

    return render(request, 'semi_app/edit_user.html', context)

def create(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for error in errors:
            messages.error(request, error)
        return redirect('/users/new')
    else:
        newUser = User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'],)
    return redirect('/users/{}'.format(User.objects.last().id))

def update(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for error in errors:
            messages.error(request, error)
        return redirect('/users/{}/edit'.format(request.POST['id']))
    else:
        newInfo = User.objects.get(id=request.POST['id'])
        newInfo.first_name = request.POST['first_name']
        newInfo.last_name = request.POST['last_name']
        newInfo.email = request.POST['email']
        newInfo.save()
        return redirect('/users/{}'.format(request.POST['id']))

def destroy(request, num):

    dead = User.objects.get(id=num)
    dead.delete()

    return redirect('/')