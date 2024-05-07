l1=list(eval(input()))
l2=list(eval(input()))
if len(l1)==len(l2):
    ll2=l2[::-1]
    for i,j in zip(l1,ll2):
        print(i,j)
else:
    print("length should be same")        