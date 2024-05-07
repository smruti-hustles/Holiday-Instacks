n=input()
v=0 #vowels
c=0 #consonants
s=0 #special symbols
d=0#digits
for i in n:
    if(i.isalpha()):
        if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
            v+=1
        else:
            c+=1
    elif(i.isdigit()):
        d=d+1
    else:
        s+=1
print(f"no of vowels {v}")     
print(f"no of consonants {c}")   
print(f"no of digits {d}")   
print(f"no of special characters or spaces {s}")      
          

