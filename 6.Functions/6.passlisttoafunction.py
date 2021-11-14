
def count(list):
    even=0;odd=0;
    for i in list:
        if i%2==0:
            even+=1
        else:
            odd+=1

    return even,odd
        
list=[20,23,45,65,87,21,12]
even, odd= count(list)

print("Even : {} and odd : {}".format(even,odd))
