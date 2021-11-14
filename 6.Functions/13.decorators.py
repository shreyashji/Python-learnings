
#can add extra features in the existing functions

def div(a,b):
 #   if a<b:
 #       a,b=b,a
    print(a/b)
#changing the way div works
def smart_div(func):
    def inner(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    return inner
div =smart_div(div)
div(2,4)

