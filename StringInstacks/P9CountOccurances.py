import re
n=input()
m=input()
a=n.lower()
b=m.lower()
res=re.findall(a,b)
print(res)
print(len(res))