n=input("Enter string : ")
res=''
for i in n:
    if i.isalnum() or i.isspace():
        res+=i
    else:
        res+='#'
print(res)          

