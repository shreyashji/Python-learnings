#all valued need to be sorted

pos=-1  #list start with 0
def Search(list,n):
    l=0
    u=len(list)-1
    while l<=u:
        mid=(l+u)//2 #inter divison
        if list[mid]==n:
           globals() ['pos']=mid
           return True
        else:
            if list[mid]<n:
                l=mid+1
            else:
                u=mid-1

list=[4,7,8,9,10,12,23,33,45,55,90]
n=10

if Search(list,n):
    print("found at",pos+1)
else:
    print("not found")
