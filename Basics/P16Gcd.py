def result(x,y):
    if x>y:
        small=x
    else:
        small=y
    for i in range(1,small+1):
        if(x%i==0 and y%i==0):
            gcd=i
    return gcd
x=int(input())             
y=int(input())             
print(result(x,y))