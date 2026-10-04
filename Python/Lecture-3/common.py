# ...existing code...
list1 = [1, 5, 9, 7, 5, 3]
list2 = [4, 5, 6, 7,9,8, 5, 2]

common = []

for x in list1:
    if x in list2 and x not in common:
        common.append(x)

print(common)