#to convert binary to octal 
#first convert binary to decimal
#then convert decimal to octal
n=input()
s=n[::-1]
sum=0
for i in range(len(s)):
    sum+=((2**i)*(int(s[i])))

n1=sum
s1=''
while(n1>0):
    r=n1%8
    s1=str(r)+s1
    n1=n1//8
print(s1)        