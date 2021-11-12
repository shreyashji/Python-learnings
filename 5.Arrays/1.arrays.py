#import array as arr
from array import *

vals=array('i',[5,9,8,4,2])
#vals=array('u',['a','b','c','d','e'])
newArr= array(vals.typecode,(a*a for a in vals))
#for i in range(len(vals)):
#for e in newArr:
i=0
while i<len(newArr):
    print(newArr[i])
    i+=1
