from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models  import User


@receiver(post_save,sender=User)
def send_noti(sender,instance,created,**kwargs):
    if created:
        print("the user is sucessfully created !!",instance.email)
