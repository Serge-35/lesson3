grades = [
    [5, 3, 3, 5, 4],
    [2, 2, 2, 3],
    [4, 5, 5, 2],
    [4, 4, 3],
    [5, 5, 5, 4, 5]
]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

b = 0
for i in grades:
    bal = grades[b]
    grades[b] = sum(bal) / len(bal)
    b = b + 1

stud_abc = list(students)
stud_abc.sort()

teacher_magazine = dict(zip(stud_abc, grades))
print(teacher_magazine)
