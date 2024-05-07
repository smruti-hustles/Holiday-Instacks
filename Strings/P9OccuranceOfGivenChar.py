print("Enter String")
n=input()
print("Enter character you wanna find the occurance")
c=input()
count=0
for i in n:
    if i==c:
        count+=1
print(f"occurance of {c} in {n} : {count} times")        