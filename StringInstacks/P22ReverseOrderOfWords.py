n=input("Enter string : ")
l=n.split(" ")
res=l[::-1]
#print(n)
#print(l)
#print(res)
s=''
for i in res:
    s+=i+' '
print(s)    