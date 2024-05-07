#  hello world------->olleh dlrow
import re
n=input()
print(n)
r=re.split(" ",n)
print(r)
s=""
for i in range(len(r)):
    t=r[i]
    t1=t[::-1]
    s=s+t1+" "
print(s)    

