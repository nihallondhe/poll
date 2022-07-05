from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from .forms import CreatePollForm,CreateUserForm
from .models import Poll
from django.contrib import messages

def home(request):
    polls = Poll.objects.all()
    context = {
        'polls' : polls
    }
    
    return render(request, 'home.html', context)

def create(request):
    if request.method == 'POST':
        form = CreatePollForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreatePollForm()
    context = {
        'form' : form
    }
    return render(request, 'create.html', context)

def vote(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)

    if request.method == 'POST':

        selected_option = request.POST['poll']
        if selected_option == 'option1':
            poll.option_one_count += 1
        elif selected_option == 'option2':
            poll.option_two_count += 1
        elif selected_option == 'option3':
            poll.option_three_count += 1
        else:
            return HttpResponse(400, 'Invalid form')

        poll.save()

        return redirect('/')

    context = {
        'poll' : poll
    }
    return render(request, 'vote.html', context)

def results(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    context = {
        'poll' : poll
    }
    return render(request, 'results.html', context)

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        '''print(username,password)'''
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            login(request)
            return render('create',{'user':user})

        else:
            messages.info(request,'Invalid credentials')
            return redirect('login')

    else:
        return render(request,'login.html')

def createuser(request):
    user = CreateUserForm()
    data = CreateUserForm(request.POST)
    if request.method == 'POST':
        if data.is_valid:
            data.save()
            data.username=user
            
            return redirect('/',user)
        else:
            return render(request,'login.html',{'user':user})


 
    return render(request,'cuser.html',{'user':user})
