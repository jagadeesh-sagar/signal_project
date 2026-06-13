from django.shortcuts import render

# Create your views here.
class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def __iter__(self):
        yield {'length': self.length}
        yield {'width': self.width}


# 1. Initialize with length and width as integers
my_rect = Rectangle(length=10, width=5)

# 2 & 3. Iterate over the instance and print the yielded values
for dimension in my_rect:
    print(dimension)