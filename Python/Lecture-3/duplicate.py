numbers = [1, 2, 3, 4, 5, 4, 3, 2, 1]
dup = []

for n in numbers:
    if n not in dup and numbers.count(n) > 1:
        dup.append(n)

print(dup)