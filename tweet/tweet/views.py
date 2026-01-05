from django.shortcuts import render
from myapp.models import tweet
from django.contrib import messages
from django.db.models import Q

def home(request):
    return render(request,'base.html')

def search(request):
    query=request.GET.get('query')
    if len(query)>100:
        results=[]
    else:
        results=tweet.objects.filter(Q(bio__icontains=query)| Q(name__username__icontains=query))
    if not results:
        messages.error(request,"no result found haha ")
    return render(request,'search.html',{'results':results,'query':query})