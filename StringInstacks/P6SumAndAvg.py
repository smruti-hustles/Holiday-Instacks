n=input("Enter marks in the following format 'Subject1=Marks1 Subject2=Marks2 ...'")
l=n.split(' ')
print(l)

total=0
no_of_subject=0

for i in l:
    subject,marks=i.split('=')
    m=int(marks)
    total+=m
    no_of_subject+=1
    print(f"{subject}={marks}")   
avg=total/no_of_subject
print(total)
print(avg)    