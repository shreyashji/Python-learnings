def person(name,**data): #** multiple data
    print(name)
    for i,j in data.items():
        print(i,j)


person('navin',age=23,city='mumbai',mob=988989)
