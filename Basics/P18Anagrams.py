p=input()
q=input()
if len(p)!=len(q):
    print("Not Anagrams")
else:
    if sorted(p)==sorted(q):
        print("Anagrams")
    else:
        print("Not Anagrams")    

