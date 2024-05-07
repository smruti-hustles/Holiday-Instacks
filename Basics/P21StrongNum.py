#sum of the factorial of its digits=number
#1,2,145,40585
def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f
n=int(input("Enter number"))
t=n
s=0
while(n>0):
    r=n%10
    s=s+fact(r)
    n=n//10
if t==s:
    print("Strong Number")
else:
    print("Not a strong number")            
