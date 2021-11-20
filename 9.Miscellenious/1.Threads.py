#threading=can run individually on same diff ore
from threading import *


from time import sleep

class hello(Thread):
    def run(self):
        for i in range(5):   
            print("hello")
            sleep(1)

class hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(1)

t1=hello()
t2=hi()

t1.start() #internally method
sleep(0.2)
t2.start()

t1.join()
t2.join()

print("bye")  #coz of main thread