def addtwo():
    c=a+b
    print(c)
    
def addtwowithparam(a,b):
    print(a+b)
    
def addtwowithreturn():
    return a+b
    
def addtwowithparmretu(x,y):
    return x+y
    
a=int(input("Enter a: "))
b=int(input("Enter b: "))

addtwo()

addtwowithparam(a,b)

print(addtwowithreturn())

print(addtwowithparmretu(a,b))




    
