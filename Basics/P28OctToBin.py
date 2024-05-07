
#to convert octal to binary 
#first convert oct to decimal
#then decimal to binary
n=input() #1000
s=n[::-1]
sum=0
for i in range(len(s)):
    sum+=((8**i)*(int(s[i])))
#print(sum)    

n1=sum
s1=''
while(n1>0):
    r=n1%2
    s1=str(r)+s1
    n1=n1//2
print(s1)    