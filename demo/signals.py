import time
from django.db.models.signals import post_save
from .models import Product
from django.dispatch import receiver
import threading


'''
question 1
'''
@receiver(post_save,sender=Product)
def signals_sync_test(sender,instance,**kwargs):
    if instance.name=='apple':
        print("\nInside signal")
        print(">> Signal triggered: Sleeping for 3 seconds...")
        time.sleep(3)
        print("Signal finished\n")

'''
question 2
'''

@receiver(post_save,sender=Product)
def signal_thread_test(sender,instance,**kwargs):

    if instance.name=='samsung':
        current_thread = threading.current_thread().ident
        print(f">> Signal running in thread: {current_thread}")
        instance._signal_thread_ident = current_thread


'''
question 3
'''
class IntentionalSignalError(Exception):
    pass

@receiver(post_save, sender=Product)
def transaction_test_handler(sender, instance, **kwargs):
    if instance.name == "lava mobile":
        print("\n>> signal triggered: Raising intentional error!")
        raise IntentionalSignalError("Forcing a rollback")
    