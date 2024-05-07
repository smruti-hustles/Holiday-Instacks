def Prime(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    if c==2:
        return True
    else:
        return False
num=int(input())  
print("Prime Factors are.....")
for j in range(2,num):  #since 1 is not prime
    if num%j==0:
        if(Prime(j)):
            print(j)