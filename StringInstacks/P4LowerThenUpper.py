n=input()
s1=''
s2=''
for i in n:
    if i.islower():
        s1+=i
for i in n:
    if i.isupper():
        s2+=i
res=s1+s2                
print(res)