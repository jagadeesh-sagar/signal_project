import time
from django.core.management.base import BaseCommand
from demo.utils import Rectangle

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        rect = Rectangle(length=20, width=10)
        for dimension in rect:
            self.stdout.write(str(dimension))