n=input()
s=n.split(" ")
print(n)
print(s)
l=[]
for i in range(len(s)):
    if i%2==0:
        l.append(s[i])
    else:
        m=s[i]
        m1=m[::-1]
        l.append(m1)    
print(l) 
res=''
for  i in l:
    res=res+i+' ' 
print(res)        
