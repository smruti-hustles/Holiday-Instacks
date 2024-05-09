#checking if a given string is starting with vowel or not
import re
n=input("Enter the string : ")
pattern=r'^[^aeiou].*$'
if re.match(pattern,n):
    print(f'{n} is starting with consonant')
else:
    print(f'{n} is not starting with consonant') 

'''
Enter the string : rohit
rohit is starting with consonant

Enter the string : apple
apple is not starting with consonant
'''    