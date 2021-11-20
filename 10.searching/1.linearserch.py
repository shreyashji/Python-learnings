pos=-1  #list start with 0
def Search(list,n):
    i=0
    while i< len(list):
        if list[i]==n:
            globals() ['pos']=i
            return True
        i=i+1
    return False

list=[5,6,876,3,2,3,8,9,10]
n=9
if Search(list,n):
    print("found at",pos+1)
else:
    print("not found")
#convert this into for loop HW