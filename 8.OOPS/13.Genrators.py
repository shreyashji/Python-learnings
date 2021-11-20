#if you need we give you genrators
#genrators give iterators
#key word yield=rmake function as a genrators
def toptens():
    n=1
    while n<=10:
        sq=n*n
        yield sq 
        n+=1


values=toptens()

print(values.__next__())

for i in values:
    print(i)