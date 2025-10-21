#  how to create a class method and operations on class
class cars:

    def __init__(self,brand,color):
        self.brand = brand
        self.color = color
        
    def drive(self):
        return f"the car of {self.brand} and color {self.color} is manual"
#   here we r taking input 
b = input("brand")
c = input("color")  
car1 = cars(b,c)
# this is object creation 
print(car1.drive())    
#if we use the print we will get none in the final output


