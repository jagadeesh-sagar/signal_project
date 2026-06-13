
class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
# instead of "return" better to use "yield" so that it can iterate 
    def __iter__(self):
        yield{'length': self.length}  
        yield{'width': self.width}


my_rect=Rectangle(length=10,width=5)
for dimension in my_rect:
    print(dimension)