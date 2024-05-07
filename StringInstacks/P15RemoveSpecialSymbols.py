s=input()
res=''
for i in s:
    if i.isalnum() or i.isspace():
        res+=i
print(res)    