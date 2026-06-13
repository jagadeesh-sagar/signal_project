import time

from django.test import TestCase
from demo.models import Product
import threading
from django.db import transaction
from demo.signals import IntentionalSignalError

class SignalTests(TestCase):

    '''
        Question 1: Are Django signals executed synchronously or asynchronously by default?

        =>by default the django signals are sync (send()) but we can change them to async too (asend()) \
        as per the offical django doc
    '''       
    ''' 
        main logic if the duration is >= 3 seconds, the caller was blocked 
        by the signal, proving synchronous execution
    '''

    def test_question_1(self):

        print("="*50)
        print('question 1:: Are Django signals executed synchronously or asynchronously by default')
        print("="*50)

        print("\nStarting object creation...")
        start_time =time.time()
        
       # it will trigger post_save signal and signals_sync_test is the reciver for this
        Product.objects.create(name="apple",price=250.01) 
        
        end_time=time.time()
        duration= end_time - start_time

        print(f"Object creation finished.Total time:{duration:} seconds")
        self.assertGreaterEqual(duration, 3)

        print("\n✓ Signal is sync.")
    



    '''
        Question 2: Do Django signals run in the same thread as the caller?

        => the ans is yes we can prove this by just checking the thread id (or) thread name 
    '''
    '''
        here both thread identifers are same showing that both run sender and reciver run on same thread
    '''

    def test_question_2(self):


        print("="*50)
        print('Question 2: Do Django signals run in the same thread as the caller?')
        print("="*50)

        caller_thread=threading.current_thread().ident
        print(f"\n>> Caller running in thread: {caller_thread}")
        
        product=Product.objects.create(name="samsung",price=444.20)

        signal_thread = getattr(product, '_signal_thread_ident', None)
        self.assertEqual(caller_thread, signal_thread, "Threads do not match!")
        
        print("\n✓ Threads match .")



    '''
        Question 3: Do Django signals run in the same database transaction as the caller?

        => 1. the ans is yes by default
           2.by default django autocommits soo. if we want to have a transaction soo we need to use
           "transaction.atomic()
           3.to prove we intentionally raise exception in signals soo that entire transaction fails 
           which proves that sender (caller)  and reciver are on same transaction

    '''

    def test_question_3(self):
        print("="*50)
        print(' Question 3: Do Django signals run in the same database transaction as the caller?')
        print("="*50)

        try:

            with transaction.atomic():
                print("Creating object within transaction block...")
                Product.objects.create(name="lava mobile",price=233.44)

        except IntentionalSignalError:
            pass
            # print("Caught the intentional error raised by the signal.")
            
        #Check object exists in the database.it won't hence proves that both r on same transaction
        exists = Product.objects.filter(name="lava mobile").exists()
        self.assertFalse(exists, "Object was saved! Transaction rollback failed.")

        print("\n✓ Transaction rollback ")
