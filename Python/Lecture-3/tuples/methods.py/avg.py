students = [
    ("Rahul", 80),
    ("Sita", 99),
    ("Siva", 100)
]

total = 0
count = 0

for name, marks in students:
    total += marks
    count += 1

avg = total / count

print(avg)