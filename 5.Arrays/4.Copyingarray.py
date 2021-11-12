from numpy import *

arr1=array([1,2,3,4,5])
arr2=array([6,1,9,3,2])
arr3=arr1+arr2
#print(arr3)

arry=array([1,2,3,4,5])
#print(sum(arry))
#print(concatenate([arr1,arr2]))
#copying
arr4=array([1,2,3,4,5])
#arr5=arr4
#view create diff location address
arr5=arr4.view()
#below is doing shallow copy
arr4[1]=7# shallow copy

arr5=arr4.copy()#deep copy
print(arr4)
print(arr5)

print(id(arr4))
print(id(arr5))