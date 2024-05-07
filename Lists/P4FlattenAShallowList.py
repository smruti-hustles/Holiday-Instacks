#merge all the sublists into a single list
#[[2,3,4],[89,90],[6,7,0]] ---> [2,3,4,89,90,6,7,0]


a= [[2, 3, 4], [89, 90], [6, 7, 0]]
l=[ele for i in a for ele in i]
print(l)

from itertools import chain
x= [[2, 3, 4], [89, 90], [6, 7, 0]]
y=list(chain.from_iterable(x))
print(y)