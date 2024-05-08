n=input("Enter string : ")
l=n.split(" ")
res=[]
for i in l:
    if any(char.isalpha() for char in i)  and any(char.isdigit() for char in i):
        res.append(i)
for j in res:
    print(j)        
    