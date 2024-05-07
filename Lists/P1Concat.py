''''
Example
Input : a=['A','B','C'], b=[1,2]
Output: ['A1','B2','C-']
'''
from itertools import zip_longest as zl
a=eval(input())
b=eval(input())
c=[i+j for i,j in zl(a,b,fillvalue='-')]
print(c)

