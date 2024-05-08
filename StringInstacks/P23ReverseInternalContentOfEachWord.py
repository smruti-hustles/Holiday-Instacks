n=input("Enter string : ")
l=n.split(" ")
res=[]
for i in l:
    s=i
    s1=s[::-1]
    res.append(s1)
print(res)    
res_str=''
for j in res:
    res_str+=j+' '
print(res_str)    
