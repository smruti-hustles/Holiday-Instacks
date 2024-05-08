n = input("Enter string: ")
s = n[::-1]
res=''
for i in s:
    if i.isdigit():
        f = int(i)
        res+=(s[s.index(i)+1]*f)
print(res)
print(res[::-1])        

'''
input: Anu5
smri3

output:
uuuuu
iii
'''        
