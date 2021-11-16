
#object in python
class Computer:

    def __init__(self,cpu,ram) :
        self.cpu=cpu
        self.ram=ram

    def config(self):
        print("Config is ",self.cpu,self.ram)

com1=Computer('i5',16)
com2=Computer('ryzen 3',8)
#print(type(com1))
#config() #wrong
#Computer.config(com1)
#Computer.config(com2)

com1.config() #we use this syntax
com2.config() #we use this syntax