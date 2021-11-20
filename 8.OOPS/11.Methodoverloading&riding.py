#polymorphism
#not in python overloading

#stdudent:
#    def average(a,b)
#   def average(a,b,c)  #this is called method overloading

#this concept is not in python
# method overriding
#same method with same parameter   (inheritance)
#method overloading below 
class Student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2

    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
                s=a+b+c
        elif a!=None and b!=None:
            s=a+b
        else:
            s=a

        return s
#method overiding below
s1=Student(58,69)
print(s1.sum(5,6,9))

class A:
    def show(self):
        print("in A show")

class B(A):
    def show(self):
        print("in B show")

a1=B()
a1.show()

