class Car:
    wheels=4                  #class namespace
    def __init__(self):
        self.mil=10           #instance namespace
        self.com="BMW"         #instance namespace

c1=Car()
c2=Car()
c1.mil=8

Car.wheels=5                       #class namespace/variables

print(c1.com,c1.mil,c1.wheels)
print(c2.com,c2.mil,c2.wheels)

#namespace is an area where you create ans store object/varibale 
#class namespace
#object/instance namespace