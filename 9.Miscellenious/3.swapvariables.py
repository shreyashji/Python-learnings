a=5
b=6
print(a)
print(b)
temp=a
a=b
b=temp
print("=====")
print(a)
print(b)

# or
a=a+b
b=a-b
a=a-b
print("=====")
print(a)
print(b)
#or
a=a^b
b=a^b
a=a^b
print("=====")
print(a)
print(b)

#or 
a,b=b,a #right solve first b,a it goes in stack and reverse & 
print("=====")
print(a)
print(b)