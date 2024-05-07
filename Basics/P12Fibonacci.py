# 0 1 1 2 3 5 8 13 21 34 55
'''
def fib(n):
    if n<=0:
        return "please enter a positive number"
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return(fib(n-1)+fib(n-2))
n=int(input())
print("Fibonacci Sequence...")   
for i in range(1,n+1):
    print(fib(i))    
'''

def fibonacci(n):
    a=0
    b=1
    if(n<=0):
        print("Enter positive number")
    elif n==1:
        return a
    elif n==2:
        return b
    else:
        for i in range(3,n+1):
            c=a+b
            a=b
            b=c
        return b    
print("Using iteration...")
num=int(input())
for i in range(1,num+1):
    print(fibonacci(i))   