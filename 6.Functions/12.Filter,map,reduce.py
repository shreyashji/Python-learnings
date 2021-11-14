
from functools import reduce
#def is_even(n):
#   return n%2==0


def add_all(a,b):
    return a+b


nums=[1,2,3,4,5,6,7,8,9,10]
evens=list(filter(lambda n: n%2==0,nums))

doubles=list(map(lambda n: n*2,evens))

sum=reduce(lambda a,b:a+b,doubles)
#print(evens)
#print(doubles)
print(sum)

#change every value we use map
#add all values use reduce