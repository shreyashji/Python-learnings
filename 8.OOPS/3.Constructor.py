#size of an objecr depends on the no. of variable and size of each variable
#who allocates size to object ,constructur
#called internally

class Computer:
    def __init__(self):
        self.name="shreyash"
        self.age=23
    
    def compare(self,other):
        if self.age==other.age:
            return True
        else:
            return False
c1=Computer()
c1.age=30
c2=Computer()

c1.name="rashi"
c2.age=12

if c1.compare(c2):
    print("they are same")
else:
    print("they are different")
print(c1.name)
print(c2.name)
