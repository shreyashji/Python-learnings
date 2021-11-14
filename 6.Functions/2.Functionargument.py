#pass by value
#pass by refrence
#everything is object there is no pass by value & pass by refrence
#its none of them

def update(list):
    print(id(list))
    list[1]=25
    print(id(list))
    print("list ",list)

#a=10
list=[10,20,30]
print(id(list))
update(list)
print("list ",list)
#print(id(a))
#update(a)
#print("a ",a)
