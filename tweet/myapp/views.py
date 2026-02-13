from django.shortcuts import render,redirect
from .models import tweet
from .forms import login,create_user
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

def home(request):
    return render(request,'index.html',{'name':'samir'}) 

def show(request):
    tweets=tweet.objects.all().order_by('-created_at')
    return render(request,'tweet.html',{'tweets':tweets})

@login_required
def create_tweet(request):
    if request.method=="POST":
        form=login(request.POST,request.FILES)
        if form.is_valid():
            tweet=form.save(commit=False)
            tweet.name=request.user
            tweet.save()
            return redirect('show')
    else:
        form=login()
    return render(request,'create.html',{'form':form})

@login_required
def edit_tweet(request,tweet_id):
    tweets=get_object_or_404(tweet,pk=tweet_id ,name=request.user)
    if request.method=="POST":
        form = login(request.POST, request.FILES, instance=tweets)
        if form.is_valid():
            form.save()
            return redirect('show')
    else:
        form=login(instance=tweets)
    return render(request,'edit.html',{'form':form})

@login_required
def tweet_delete(request,tweet_id):
    form=get_object_or_404(tweet,pk=tweet_id,name=request.user)
    if request.method=="POST":
        form.delete()
        return redirect('show')
    return render(request,'delete.html')

def register(request):
    if request.method=='POST':
        form=create_user(request.POST)
        if form.is_valid():
            user=form.save()
            login(request, user)
            return redirect('show')
    else:
        form=create_user()
    return render(request,'registration/register.html',{'form':form})

