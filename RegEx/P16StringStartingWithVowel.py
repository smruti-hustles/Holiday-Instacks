#checking if a given string is starting with vowel or not
import re
n=input("Enter the string : ")
pattern=r'^[aeiou].*$'
if re.match(pattern,n):
    print(f'{n} is starting with vowel')
else:
    print(f'{n} is not starting with vowel') 