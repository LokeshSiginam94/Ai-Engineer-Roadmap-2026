tup=(10,20)
a,b=tup
print("a=",a)
print("b=",b)
b,a=a,b
print("a=",a)
print("b=",b)

#or
a,b=tup
a,b=b,a
print("a=",a)
print("b=",b)