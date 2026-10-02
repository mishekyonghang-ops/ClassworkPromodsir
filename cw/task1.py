name = input("Enter student name: ")
marks = []

for i in range(1, 4):
    marks.append(float(input(f"Enter marks in subject {i}: ")))

m1, m2, m3 = marks

total = m1 + m2 + m3
average = total / 3

if average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"

pass_mark = 40
if m1 >= pass_mark and m2 >= pass_mark and m3 >= pass_mark:
    result = "Pass"
else:
    result = "Fail"

print(f"\nStudent: {name}")
print(f"Total: {total}")
print(f"Average: {average:.1f}")
print(f"Grade: {grade}")
print(f"Result: {result}")

print("\nSubject marks:")
for i in range(3):
    print(f"Subject {i + 1}: {marks[i]}")