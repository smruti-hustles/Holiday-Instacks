print("Enter String")
n=input()
print("Enter character you wanna remove")
c=input()
s=''
for i in n:
    if i!=c:
        s=s+i
print(s)        
