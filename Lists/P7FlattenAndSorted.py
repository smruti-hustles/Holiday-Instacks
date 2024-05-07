from itertools import chain
# Take input from the user for the number of sublists
n = int(input("Enter the number of sublists: "))
# Initialize an empty list to store the sublists
sublists = []
# Take input for each sublist
for i in range(n):
    sublist_input = input(f"Enter sublist {i + 1} (space-separated values): ")
    sublist = [int(x) for x in sublist_input.split()]
    sublists.append(sublist)
# Flatten the list of sublists into a single list
merged_list = list(chain.from_iterable(sublists))
# Output the merged list
print("Merged list:", merged_list)
s=set(merged_list)
print(sorted(s))