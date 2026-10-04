# ...existing code...
nested = [[1, 2], [3, 4]]

flat = []

for row in nested:
    for num in row:
        flat.append(num)

print(flat)