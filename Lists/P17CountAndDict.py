from collections import Counter
    
def result(n):
    res=Counter(tuple(i) for i in n)
    return  res
    #return {key:value for key,value in res.items() if value>0}


n=list(eval(input()))
print(result(n))