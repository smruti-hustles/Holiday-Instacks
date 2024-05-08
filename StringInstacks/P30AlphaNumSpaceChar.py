m=input()
n=sorted(m)
alpha=''
num=''
space=''
char=''
for i in n:
    if i.isalpha():
        alpha+=i
    elif i.isdigit():
        num+=i
    elif i.isspace():
        space+=i 
    else:
        char+=i           
res=alpha+num+space+char
print(res)        