#checking if a given variable name is valid or not
import re
n=input("Enter the variable name : ")
pattern=r'^[a-zA-Z_][a-zA-Z0-9_]*$'
if re.match(pattern,n):
    print(f'{n} is valid')
else:
    print(f'{n} is not valid')    
