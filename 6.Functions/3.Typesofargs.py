def person(name,age):  #formal args
    print(name)
    print(age)

person("navin",6) 
#positon args
#default args
#keyword args
#variable length args

#keyword args
def person2(name,age):  #formal args
    print(name)
    print(age)

person2(name="navin",age=15) 

#default args
def person3(name,age=18):  #formal args
    print(name)
    print(age)

person3('navin') 


#variable length args
def sum(a,*b):
    c=a
    for i in b:
        c=c+i

    print(c)

sum(5,6,34,78)