
n=int(input("Enter till where you want to print the prime numbers "))
for i in range(1,n+1):
    c=0
    for j in range(1,i+1):
        if i%j==0:
            c+=1
    if c==2:
        print(i)  
        '''
#prime numbers between 1 to k
k=int(input())
for i in range(1,k+1):
    c=0
    for j in range(1,i+1):
        if(i%j==0):
            c+=1 
    if(c==2):
        print(i)            
        '''