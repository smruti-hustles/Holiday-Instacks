n=int(input())
t=n
sum=0
while(n!=0):
    r=n%10
    sum=sum+r 
    n=n//10
print(f"sum of digits of {t} is {sum}")      
