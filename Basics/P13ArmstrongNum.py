s=input()
l=len(s)
n=int(s)
t=n
sum=0
while(n!=0):
    r=n%10
    sum=sum+(r**l)
    n=n//10
if t==sum:
    print("Armstrong number")    
else:
    print("Not an Armstrong number")    
 #153,370,407,8280,1,2,3,4,6,5,7,8,9,93084,548834
     