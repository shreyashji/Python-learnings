class Student:              #outer class
   
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        self.lap=self.Laptop()

    def show(self):
        print(self.name,self.rollno)
        self.lap.show()
    class Laptop:       #inner class
        def __init__(self):
            self.brand='HP'
            self.cpu='i5'
            self.ram=8

        def show(self):
            print(self.brand,self.cpu,self.ram)

s1=Student('SHALWA',2)
s2=Student('HALWA',3)
s2.show()

#lap1=Student.Laptop()
#lap2=Student.Laptop()

#print(id(lap1))
#print(id(lap2))