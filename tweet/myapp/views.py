from django.shortcuts import render,redirect
from .models import tweet
from django.contrib.auth.models import User
from .forms import login,create_user
from django.template.loader import render_to_string
from django.http import HttpResponse,JsonResponse
from django.utils.html import strip_tags
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from django.core.cache import cache
from django_ratelimit.decorators import ratelimit
from .tasks import add,mul
from celery.result import AsyncResult


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

def mail_to_be_sent(request):
    subject = 'this is our welcome mail'
    html_content=render_to_string('email.html',{'name':"samir","otp_code":"978645"})
    plain_text=strip_tags(html_content)
    message=plain_text
    recipient_list=['aryalsamir629@gmail.com']

    send_mail(
        subject,
        message,
        None,
        recipient_list,
        html_message=html_content
    )
    return HttpResponse("Mail actually sent!")

def redis(request):
    list=[] 
    if cache.get('details',default=None):
         list=cache.get('details')
         db='redis'

    else:
        data=User.objects.all()
        for i in data:
            list.append(i.username)
            db='sqlite'

            cache.set('details',list,timeout=20)
        
    return JsonResponse({'data':list,'dbname':db,'status':200})

@ratelimit(key='user_or_ip',rate='5/m',block=False)
def rate_limit(request):
    if request.limited==True:
        return JsonResponse({'status':200,'result':"too many tries"})
    return JsonResponse({'status':200,'result':"sucess"})


def celery(request):
    result=mul.apply_async(args=[2,5])
    return render(request,'tweet.html',{'result':result})
    
def results(request,id):
    result=AsyncResult(id)
    return render(request,'celery.html',{'result':result})