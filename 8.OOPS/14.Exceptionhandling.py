

a=5
b=2

try:
    print("resource open")
    print(a/b)
    k=int(input("enter a number"))
    print(k)
except ZeroDivisionError as e:
    print("HEY, YOU CANNOT divide a number by zero",e)

except ValueError as e:
    print("INVALID INPUT",e)

except Exception as e:
    print("SOMETHING WENT WRONG",e)


finally:
    print("resource closed")
