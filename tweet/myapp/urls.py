from django.urls import path
from .import views 

urlpatterns = [
     path('',views.show,name='show'),
     path('<int:tweet_id>/delete/',views.tweet_delete,name='delete'),
     path('create/',views.create_tweet,name='create'),
     path('<int:tweet_id>/edit/',views.edit_tweet,name='edit'),
     path('register/',views.register,name='register'),
     path('mail/',views.mail_to_be_sent,name='mail'),
     path('redis/',views.redis,name='redis'),
     path('ratelimit/',views.rate_limit,name='ratelimit'),
     path('celery/',views.celery,name='celery'),
     path('results/<str:id>/',views.results,name='results'),
]

