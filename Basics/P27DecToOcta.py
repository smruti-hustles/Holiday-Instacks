n=int(input())
s=''
while(n>0):
    r=n%8
    s=str(r)+s
    n=n//8
print(s)    